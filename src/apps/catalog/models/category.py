from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from apps.catalog.constants import STATUS_CHOICES


class Category(MPTTModel):
    """
    Категории товаров
    """

    order = models.IntegerField(verbose_name='порядок отображения', unique=True)
    name = models.CharField(max_length=100, verbose_name='название')
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subcategories',
        verbose_name='родительская категория',
    )
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='статус')

    class MPTTMeta:
        """
        Сортировка по названию
        """
        order_insertion_by = ('name',)

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('order',)

    def __str__(self) -> str:
        return self.name
