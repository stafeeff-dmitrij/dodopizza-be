from django.db import models

from apps.catalog.models import Category
from apps.catalog.models.base import BaseModel
from apps.catalog.utils.image import get_ingredient_image_path


class Ingredient(BaseModel):
    """
    Ингредиенты
    """

    name = models.CharField(max_length=100, verbose_name='название', unique=True)
    image = models.ImageField(upload_to=get_ingredient_image_path, verbose_name='изображение')

    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE,
                                 related_name='ingredients', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'ingredients'
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
