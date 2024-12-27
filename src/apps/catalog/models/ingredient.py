from django.db import models

from apps.catalog.constants import STATUS_CHOICES
from apps.catalog.utils.image import get_ingredient_image_path


class Ingredient(models.Model):
    """
    Ингредиенты
    """

    order = models.PositiveIntegerField(verbose_name='порядок отображения')
    name = models.CharField(max_length=100, verbose_name='название', unique=True)
    price = models.PositiveIntegerField(verbose_name='стоимость')
    image = models.ImageField(upload_to=get_ingredient_image_path, verbose_name='изображение')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='статус')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'ingredients'
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
