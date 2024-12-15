from rest_framework import serializers

from apps.catalog.models import Category


class CategoryBaseSerializer(serializers.ModelSerializer):
    """
    Схема с основными полями для вывода данных по категориям
    """

    id = serializers.IntegerField()
    name = serializers.CharField()


class SubCategorySerializer(CategoryBaseSerializer):
    """
    Схема для вывода данных о вложенной категорий товаров
    """

    class Meta:
        model = Category
        fields = ('id', 'name')


class CategorySerializer(CategoryBaseSerializer):
    """
    Схема для вывода данных по категориям
    """

    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'subcategories')
