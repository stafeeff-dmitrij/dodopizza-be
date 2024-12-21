from django.db import models

from apps.catalog.constants import STATUS_CHOICES


class Category(models.Model):
    """
    Категории товаров
    """

    order = models.IntegerField(verbose_name='порядок отображения')
    name = models.CharField(max_length=100, verbose_name='название')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='статус')

    class Meta:
        db_table = 'categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('order',)

    def __str__(self) -> str:
        return self.name
