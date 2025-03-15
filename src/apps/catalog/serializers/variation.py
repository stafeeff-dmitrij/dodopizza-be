from rest_framework import serializers

from apps.catalog.models import Variation
from apps.catalog.serializers.ingredient import IngredientVariationSerializer
from apps.catalog.utils.image import get_url_image


class VariationSerializer(serializers.ModelSerializer):
    """
    Схема для вывода вариаций товара
    """

    image = serializers.SerializerMethodField()
    ingredients = IngredientVariationSerializer(many=True)

    def get_image(self, obj) -> str | None:
        """
        Возврат изображения ингредиента
        """
        return get_url_image(obj.image.url)

    class Meta:
        model = Variation
        fields = (
            'id', 'price', 'image', 'pizza_size', 'pizza_type', 'count', 'portion_size', 'volume', 'weight',
            'mass', 'ingredients',
        )
