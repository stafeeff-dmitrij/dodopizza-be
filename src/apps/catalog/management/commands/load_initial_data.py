from django.core.management import call_command
from django.core.management.base import BaseCommand

from apps.catalog.models import (
    Category,
    Ingredient,
    Product,
    Variation,
    VariationToIngredient,
)


class Command(BaseCommand):
    """
    Загрузка фикстур при отсутствии данных в БД
    """
    help = 'Проверка и загрузка фикстур при отсутствии данных в БД'

    def handle(self, *args, **options):

        if not Category.objects.exists():
            self.stdout.write(self.style.WARNING(
                'Отсутствуют данные по категориям товаров. Загрузка категорий из фикстур.'))
            call_command('loaddata', '../fixtures/1-categories.json')
        else:
            self.stdout.write(self.style.SUCCESS(
                'В БД присутствуют данные о категориях товаров, импорт фикстур не требуется.'))

        if not Ingredient.objects.exists():
            self.stdout.write(self.style.WARNING(
                'Отсутствуют данные по ингредиентам. Загрузка ингредиентов из фикстур.'))
            call_command('loaddata', '../fixtures/2-ingredients.json')
        else:
            self.stdout.write(self.style.SUCCESS(
                'В БД присутствуют данные об ингредиентах, импорт фикстур не требуется.'))

        if not Product.objects.exists():
            self.stdout.write(self.style.WARNING('Отсутствуют данные по товарам. Загрузка товаров из фикстур.'))
            call_command('loaddata', '../fixtures/3-products.json')
        else:
            self.stdout.write(self.style.SUCCESS('В БД присутствуют данные о товарах, импорт фикстур не требуется.'))

        if not Variation.objects.exists():
            self.stdout.write(self.style.WARNING(
                'Отсутствуют данные по вариациям товаров. Загрузка данных из фикстур.'))
            call_command('loaddata', '../fixtures/4-variations.json')
        else:
            self.stdout.write(self.style.SUCCESS(
                'В БД присутствуют данные по вариациям товаров, импорт фикстур не требуется.'))

        if not VariationToIngredient.objects.exists():
            self.stdout.write(self.style.WARNING(
                'Отсутствуют данные по связям между вариациям и ингредиентам. Загрузка данных из фикстур.'))
            call_command('loaddata', '../fixtures/5-variationtoingredient.json')
        else:
            self.stdout.write(self.style.SUCCESS(
                'В БД присутствуют данные по связям между вариациями и ингредиентам, импорт фикстур не требуется.'))
