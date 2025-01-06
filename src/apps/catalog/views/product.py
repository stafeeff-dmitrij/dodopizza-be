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
        Фильтрация товаров по номеру категории
        """
        category_id = self.request.query_params.get('category_id')

        if category_id:
            products = Product.objects.filter(categories__id=category_id).order_by('order')
        else:
            products = Product.objects.all().order_by('order')

        return products

    @extend_schema(
        parameters=[
            OpenApiParameter(name='category_id', description='id категории', required=False, type=int),
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

    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
