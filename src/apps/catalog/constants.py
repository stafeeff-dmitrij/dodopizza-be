from django.db import models


class PizzaSizeChoice(models.IntegerChoices):
    """
    Типы размеров пицц
    """
    small = 25, '25 см'
    average = 30, '30 см'
    big = 35, '35 см'


class PizzaTypeChoice(models.TextChoices):
    """
    Типы теста пицц
    """
    traditional = 'traditional', 'Традиционное'
    slim = 'slim', 'Тонкое'


class ProductCountChoice(models.IntegerChoices):
    """
    Кол-во товара
    """
    one = 1, '1 шт'
    two = 2, '2 шт'
    three = 3, '3 шт'
    four = 4, '4 шт'
    five = 5, '5 шт'
    eight = 8, '8 шт'
    ten = 10, '10 шт'
    sixteen = 16, '16 шт'


class PortionSizeChoice(models.TextChoices):
    """
    Размеры порций
    """
    small = 'small', 'Маленькая'
    average = 'average', 'Средняя'
    big = 'big', 'Большая'


class DrinkVolumeChoice(models.TextChoices):
    """
    Объемы напитков
    """
    vol_0_3_liters = '0.3', '0.3 л'
    vol_0_4_liters = '0.4', '0.4 л'
    vol_0_45_liters = '0.45', '0.45 л'
    vol_0_5_liters = '0.5', '0.5 л'
    vol_1_0_liters = '1', '1 л'


class WeightChoice(models.TextChoices):
    """
    Вес рассыпного товара
    """
    half_kilo = '0.5', '0.5 кг'


STATUS_CHOICES = [
    (True, 'Активно'),
    (False, 'Не активно'),
]


class CategoryType(models.IntegerChoices):
    """
    id категорий
    """
    pizza = 2, 'Пицца'
