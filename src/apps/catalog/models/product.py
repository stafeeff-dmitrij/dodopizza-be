from django.db import models

from apps.catalog.constants import STATUS_CHOICES
from apps.catalog.models import Category


class Product(models.Model):
    """
    Товары
    """

    name = models.CharField(max_length=100, verbose_name='название')
    description = models.CharField(max_length=200, verbose_name='описание')
    # TODO Картинка будет у вариаций
    # image = models.ImageField(upload_to=get_product_image_path, blank=True, null=True, verbose_name='изображение')
    count = models.PositiveIntegerField(verbose_name='количество')
    category = models.ForeignKey(Category, verbose_name='категория', on_delete=models.CASCADE)
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='статус')

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
