import logging

from rest_framework import serializers

from apps.catalog.constants import CategoryType, PizzaSizeChoice, PizzaTypeChoice
from apps.catalog.models import Category, Product
from apps.catalog.serializers.ingredient import IngredientProductSerializer
from apps.catalog.serializers.variation import VariationSerializer
from apps.catalog.utils.image import get_full_url_image

logger = logging.getLogger(__name__)


class ProductSerializer(serializers.ModelSerializer):
    """
    Схема для вывода данных по товару
    """

    image = serializers.SerializerMethodField('get_image')
    min_price = serializers.SerializerMethodField('get_min_price')
    variation_have = serializers.SerializerMethodField('get_variation_have')

    def get_image(self, obj) -> str | None:
        """
        Возврат изображения товара
        """
        variations = obj.variation_set.all().order_by('order')

        if obj.parent_category_id == CategoryType.pizza:
            # для пицц возврат картинки по умолчанию 30 см, традиционное
            variation = variations.filter(
                pizza_size=PizzaSizeChoice.average,
                pizza_type=PizzaTypeChoice.traditional
            ).first()
        else:
            variation = variations.first()

        if variation:
            return get_full_url_image(variation.image.url)

    def get_min_price(self, obj) -> int | None:
        """
        Возврат минимальной цены товара
        """
        variation = obj.variation_set.order_by('price').first()

        if variation:
            return variation.price

    def get_variation_have(self, obj) -> bool:
        """
        Возврат флага о наличии вариаций у товара
        """
        variation_count = obj.variation_set.count()
        return variation_count > 1

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'image', 'min_price', 'variation_have', 'count')


class AllProductsSerializer(serializers.ModelSerializer):
    """
    Схема для вывода товаров в связке к категориям, которым они принадлежат
    """

    products = serializers.SerializerMethodField('get_active_products')

    def get_active_products(self, obj) -> float:
        """
        Возврат активных товаров
        """
        active_products = obj.products.filter(status=True).order_by('order')[:12]
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
    default_ingredients = serializers.SerializerMethodField('get_ingredients')
    variations = serializers.SerializerMethodField('get_variations')

    def get_ingredients(self, obj) -> float:
        """
        Возврат дефолтных ингредиентов товара
        """
        records = obj.ingredients.filter(status=True).order_by('order')
        serializer = IngredientProductSerializer(records, many=True)

        return serializer.data

    def get_variations(self, obj) -> float:
        """
        Возврат вариаций товара
        """
        variations = obj.variation_set.filter(status=True).order_by('order')
        serializer = VariationSerializer(variations, many=True)

        return serializer.data

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'count', 'category_id', 'default_ingredients', 'variations')
