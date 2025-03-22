from django.http import QueryDict
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, mixins, status, viewsets

from apps.catalog.models import Product
from apps.catalog.pagination import CatalogPagination
from apps.catalog.querysets import (
    get_all_product_queryset,
    get_filter_product_queryset,
    get_product_detail_queryset,
)
from apps.catalog.serializers.product import (
    AllProductsSerializer,
    ProductDetailSerializer,
    ProductSerializer,
)
from apps.catalog.services import ProductFilterServices
from config.settings import CACHE_TIMEOUT


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class AllProductsListView(viewsets.ModelViewSet):
    """
    Возврат товаров в связке к категориям, которым они принадлежат
    """

    queryset = get_all_product_queryset()
    serializer_class = AllProductsSerializer
    pagination_class = None

    @extend_schema(
        summary='Возврат товаров для главной страницы',
        description='Возврат товаров в связке к категориям, которым они принадлежат',
        responses={
            status.HTTP_200_OK: AllProductsSerializer,
        }
    )
    def list(self, request):
        return super().list(request)


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class ProductsFilterListView(generics.GenericAPIView, mixins.ListModelMixin):
    """
    Возврат товаров
    """

    serializer_class = ProductSerializer
    pagination_class = CatalogPagination

    def get_queryset(self) -> QueryDict[Product]:
        """
        Фильтрация и сортировка товаров
        """
        params = self.request.query_params
        products = ProductFilterServices.get_products(params=params)
        queryset = get_filter_product_queryset(queryset=products)

        return queryset

    @extend_schema(
        summary='Возврат товаров',
        description='Фильтрация и сортировка товаров',
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

    queryset = get_product_detail_queryset()
    serializer_class = ProductDetailSerializer

    @extend_schema(
        summary='Возврат товара',
        description='Возврат детальной информации о товаре',
        responses={
            status.HTTP_200_OK: ProductDetailSerializer,
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
