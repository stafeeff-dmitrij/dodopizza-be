from rest_framework import serializers

from apps.catalog.models import Variation
from apps.catalog.serializers.ingredient import IngredientVariationSerializer
from apps.catalog.utils.image import get_full_url_image


class VariationSerializer(serializers.ModelSerializer):
    """
    Схема для вывода вариаций товара
    """

    image = serializers.SerializerMethodField('get_image')
    ingredients = serializers.SerializerMethodField('get_ingredients')

    def get_image(self, obj) -> str | None:
        """
        Возврат изображения ингредиента
        """
        return get_full_url_image(obj.image.url)

    def get_ingredients(self, obj) -> float:
        """
        Возврат ингредиентов
        """
        records = obj.variationtoingredient_set.filter(ingredient__status=True).order_by('order')
        serializer = IngredientVariationSerializer(records, many=True)

        return serializer.data

    class Meta:
        model = Variation
        fields = (
            'id', 'price', 'image', 'pizza_size', 'pizza_type', 'count', 'portion_size', 'volume', 'weight',
            'mass', 'ingredients',
        )
