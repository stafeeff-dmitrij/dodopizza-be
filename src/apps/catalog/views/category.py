from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from apps.catalog.models import Category
from apps.catalog.serializers import CategorySerializer


@extend_schema(tags=['Каталог'])
class CategoryListView(viewsets.ModelViewSet):
    """
    Возврат категорий товаров
    """

    queryset = Category.objects.filter(status=True).order_by('order')
    serializer_class = CategorySerializer
