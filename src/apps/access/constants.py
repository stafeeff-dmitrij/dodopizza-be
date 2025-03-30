from django.db import models


class AccessPeriodChoice(models.TextChoices):
    """
    Варианты периода предоставления доступа
    """
    TEN_MIN = '10m', '10 минут'
    THIRTY_MIN = '30m', '30 минут'
    ONE_HOUR = '1h', '1 час'
    TWO_HOUR = '2h', '2 часа'
    SIX_HOUR = '6h', '6 часов'
    TWELVE_HOUR = '12h', '12 часов'
    ONE_DAY = '1d', '1 день'
    ONE_WEEK = '1w', '1 неделя'
    ONE_MONTH = '1M', '1 месяц'
    ALWAYS = 'always', 'Всегда'
