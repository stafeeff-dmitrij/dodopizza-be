from rest_framework import serializers

from apps.catalog.models import Category
from apps.catalog.serializers.product import ProductSerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных по категориям
    """

    products = serializers.SerializerMethodField("get_active_products")

    def get_active_products(self, obj) -> float:
        """
        Возврат активных товаров
        """
        active_products = obj.product_set.filter(status=True)[:12]
        serializer = ProductSerializer(active_products, many=True)

        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')
