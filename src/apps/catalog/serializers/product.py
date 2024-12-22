from rest_framework import serializers

from apps.catalog.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных по товару
    """

    image = serializers.CharField(
        default='https://media.dodostatic.net/image/r:292x292/11ef9050501f3fa690a64053f5f07626.jpg')

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'count')
