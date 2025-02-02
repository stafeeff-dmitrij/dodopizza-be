from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, mixins, viewsets

from apps.catalog.models import Category, Product
from apps.catalog.pagination import CatalogPagination
from apps.catalog.serializers.product import (
    AllProductsSerializer,
    ProductDetailSerializer,
    ProductSerializer,
)
from apps.catalog.services import FilterAndSortProductServices
from config.settings import CACHE_TIMEOUT


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class AllProductsListView(viewsets.ModelViewSet):
    """
    Возврат товаров в связке к категориям, которым они принадлежат
    """

    queryset = Category.objects.filter(status=True).order_by('order')
    serializer_class = AllProductsSerializer
    pagination_class = None


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class ProductsFilterListView(generics.GenericAPIView, mixins.ListModelMixin):
    """
    Возврат товаров
    """

    serializer_class = ProductSerializer
    pagination_class = CatalogPagination

    def get_queryset(self) -> list[Product]:
        """
        Фильтрация и сортировка товаров
        """
        params = self.request.query_params
        products = FilterAndSortProductServices.get_products(params=params)

        return products

    @extend_schema(
        parameters=[
            OpenApiParameter(name='search', description='Поиск по названию', required=False, type=str),
            OpenApiParameter(name='category_id', description='id категории', required=False, type=int),
            OpenApiParameter(name='min_price', description='Минимальная цена', required=False, type=int),
            OpenApiParameter(name='max_price', description='Максимальная цена', required=False, type=int),
            OpenApiParameter(name='ingredients', description='Ингредиенты', required=False, type=str),
            OpenApiParameter(name='in_have', description='Только товары в наличии', required=False, type=bool),
            OpenApiParameter(name='sort', description='Сортировка: name, price', required=False, type=str),
        ],
    )
    def get(self, request):
        return self.list(request)


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class ProductDetailView(generics.RetrieveAPIView):
    """
    Возврат детальной информации о товаре
    """

    queryset = Product.objects.filter(status=True)
    serializer_class = ProductDetailSerializer
