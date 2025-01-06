from rest_framework import serializers

from apps.catalog.models import Ingredient, VariationToIngredient
from apps.catalog.utils.image import get_full_url_image


class IngredientVariationSerializer(serializers.ModelSerializer):
    """
    Схема для вывода ингредиентов вариации товара
    """

    id = serializers.IntegerField(source='ingredient_id')
    name = serializers.CharField(source='ingredient.name')
    image = serializers.SerializerMethodField('get_image')

    def get_image(self, obj) -> str | None:
        """
        Возврат изображения ингредиента
        """
        return get_full_url_image(obj.ingredient.image.url)

    class Meta:
        model = VariationToIngredient
        fields = ('id', 'name', 'image', 'price')


class IngredientProductSerializer(serializers.ModelSerializer):
    """
    Схема для вывода ингредиентов по умолчанию для товара
    """

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
