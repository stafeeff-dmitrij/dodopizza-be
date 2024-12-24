from rest_framework import serializers

from apps.catalog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных по категориям
    """

    class Meta:
        model = Category
        fields = ('id', 'name')
