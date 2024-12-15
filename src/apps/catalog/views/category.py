from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.catalog.models import Category
from apps.catalog.serializers import CategorySerializer
from config.settings import CACHE_TIMEOUT


@extend_schema(tags=['Каталог'])
@method_decorator(cache_page(CACHE_TIMEOUT), name='dispatch')
class CategoryListView(viewsets.ModelViewSet):
    """
    Возврат категорий товаров
    """

    queryset = Category.objects.filter(parent=None, status=True).order_by('order')
    serializer_class = CategorySerializer
