from django.db import models

from apps.catalog.constants import STATUS_CHOICES
from apps.catalog.models import Category


class Product(models.Model):
    """
    Товары
    """

    order = models.PositiveIntegerField(verbose_name='порядок отображения')
    name = models.CharField(max_length=100, verbose_name='название', unique=True, db_index=True)
    description = models.CharField(max_length=200, verbose_name='описание', null=True, blank=True)
    count = models.PositiveIntegerField(verbose_name='количество')
    categories = models.ManyToManyField(Category, verbose_name='категория')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='статус')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
