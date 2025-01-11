# чтобы avif-формат изображений корректно сохранялся через ImageField
# noqa - чтобы не ругался flake8 при форматировании кода
import pillow_avif  # noqa
from django.db import models

from apps.catalog.constants import (
    DrinkVolumeChoice,
    PizzaSizeChoice,
    PizzaTypeChoice,
    PortionSizeChoice,
    ProductCountChoice,
    WeightChoice,
)
from apps.catalog.models.base import BaseModel
from apps.catalog.models.ingredient import Ingredient
from apps.catalog.models.product import Product
from apps.catalog.utils import get_variation_image_path


class Variation(BaseModel):
    """
    Вариации товаров
    """

    price = models.PositiveIntegerField(verbose_name='стоимость, руб')
    image = models.ImageField(upload_to=get_variation_image_path, verbose_name='изображение')
    pizza_size = models.IntegerField(verbose_name='размер пиццы', choices=PizzaSizeChoice, blank=True, null=True)
    pizza_type = models.CharField(verbose_name='тип теста', choices=PizzaTypeChoice, blank=True, null=True)
    count = models.IntegerField(verbose_name='кол-во, шт.', choices=ProductCountChoice, blank=True, null=True)
    portion_size = models.CharField(verbose_name='размер порции', choices=PortionSizeChoice, blank=True, null=True)
    volume = models.CharField(verbose_name='объем, л', choices=DrinkVolumeChoice, blank=True, null=True)
    weight = models.CharField(verbose_name='масса, кг', choices=WeightChoice, blank=True, null=True)
    mass = models.IntegerField(verbose_name='масса, г', blank=True, null=True)

    product = models.ForeignKey(Product, verbose_name='товар', on_delete=models.CASCADE, related_name='variations')
    ingredients = models.ManyToManyField(Ingredient, verbose_name='доп.ингредиенты', through='VariationToIngredient')

    def __str__(self) -> str:
        return f'Товар: {self.product.name}'

    class Meta:
        db_table = 'variations'
        verbose_name = 'Вариация'
        verbose_name_plural = 'Вариации'


class VariationToIngredient(models.Model):
    """
    Связь между вариациями и ингредиентами с доп.полем 'стоимость'
    """

    order = models.PositiveIntegerField(verbose_name='порядок отображения', blank=True, null=True)
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(verbose_name='стоимость')

    def save(self, *args, **kwargs):
        """
        Авто подстановка порядкового номера отображения при создании записи
        """
        if not self.order:
            last_record = VariationToIngredient.objects.filter(variation=self.variation).order_by('order').last()
            if last_record:
                self.order = last_record.order + 1
            else:
                self.order = 1
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.id}. {self.ingredient.name}'

    class Meta:
        db_table = 'variation_to_ingredient'
        verbose_name = 'Вариация-ингредиент'
        verbose_name_plural = 'Вариации-ингредиенты'
        unique_together = (('variation', 'ingredient'),)
