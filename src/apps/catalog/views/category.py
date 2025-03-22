from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets

from apps.catalog.models import Category
from apps.catalog.serializers.category import CategorySerializer
from config.settings import CACHE_TIMEOUT


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class CategoryListView(viewsets.ModelViewSet):
    """
    Возврат категорий
    """

    # активные категории с активными товарами с активными вариациями
    queryset = (
        Category.objects
        .filter(status=True, products__status=True, products__variations__status=True)
        .order_by('order').distinct()
    )
    serializer_class = CategorySerializer
    pagination_class = None

    @extend_schema(
        summary='Возврат категорий товаров',
        description='Возврат всех категорий товаров',
        responses={
            status.HTTP_200_OK: CategorySerializer,
        }
    )
    def list(self, request):
        return super().list(request)
