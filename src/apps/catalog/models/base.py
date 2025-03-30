from django.db import models

from apps.catalog.constants import STATUS_CHOICES


class BaseModel(models.Model):
    """
    Абстрактная модель с базовыми повторяющимися полями
    """

    order = models.PositiveIntegerField(verbose_name='порядок отображения')
    status = models.BooleanField(choices=STATUS_CHOICES, default=True, verbose_name='статус')

    class Meta:
        abstract = True
