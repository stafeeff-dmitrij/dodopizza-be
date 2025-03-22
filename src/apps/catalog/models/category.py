from django.db import models

from apps.catalog.models.base import BaseModel


class Category(BaseModel):
    """
    Категории товаров
    """

    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('order',)
