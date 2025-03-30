from django.db import models

from apps.catalog.models.base import BaseModel
from apps.catalog.models.category import Category
from apps.catalog.models.ingredient import Ingredient


class Product(BaseModel):
    """
    Товары
    """

    name = models.CharField(max_length=100, verbose_name='название', unique=True, db_index=True)
    description = models.CharField(max_length=200, verbose_name='описание', null=True, blank=True)
    count = models.PositiveIntegerField(verbose_name='количество')

    parent_category = models.ForeignKey(Category, verbose_name='основная категория',
                                        on_delete=models.CASCADE, related_name='product')
    categories = models.ManyToManyField(Category, verbose_name='категории', related_name='products')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='ингредиенты', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
