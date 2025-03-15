import logging

from rest_framework import serializers

from apps.catalog.models import Category, Product
from apps.catalog.serializers.ingredient import IngredientProductSerializer
from apps.catalog.serializers.variation import VariationSerializer
from apps.catalog.utils.image import get_url_str_image

logger = logging.getLogger(__name__)


class ProductSerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных по товару
    """

    image = serializers.SerializerMethodField()
    min_price = serializers.IntegerField()
    variations_have = serializers.SerializerMethodField()

    def get_image(self, obj) -> str | None:
        """
        Возврат изображения товара
        """
        try:
            return get_url_str_image(obj.image) if obj.image else None
        except AttributeError:
            logger.error('Не найдено изображение товара')
            pass

    def get_variations_have(self, obj) -> bool:
        """
        Возврат флага о наличии вариаций у товара
        """
        return obj.variations.count() > 1

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'min_price', 'variations_have', 'count')


class AllProductsSerializer(serializers.ModelSerializer):
    """
    Схема для вывода товаров в связке к категориям, которым они принадлежат
    """

    products = serializers.SerializerMethodField('get_active_products')

    def get_active_products(self, obj) -> float:
        """
        Возврат активных товаров
        """
        active_products = obj.products.all()[:12]
        serializer = ProductSerializer(active_products, many=True)

        return serializer.data

    class Meta:
        model = Category
        fields = ('id', 'name', 'products')


class ProductDetailSerializer(serializers.ModelSerializer):
    """
    Схема для вывода детальной информации о товаре
    """

    category_id = serializers.IntegerField(source='parent_category_id')
    default_ingredients = IngredientProductSerializer(source='ingredients', many=True)
    variations = VariationSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'count', 'category_id', 'default_ingredients', 'variations')
