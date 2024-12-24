from rest_framework import serializers

from apps.catalog.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных по товару
    """

    image = serializers.CharField(
        default='https://media.dodostatic.net/image/r:292x292/11ef9050501f3fa690a64053f5f07626.jpg'
    )

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'count')


class AllProductsSerializer(serializers.ModelSerializer):
    """
    Схема для вывода товаров в связке к категориям, которым они принадлежат
    """

    products = serializers.SerializerMethodField('get_active_products')

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
