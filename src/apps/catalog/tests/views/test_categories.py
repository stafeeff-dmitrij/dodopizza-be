from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.catalog.models import Category, Product, Variation
from apps.catalog.tests.base import TestBase


class TestCategoryListView(TestBase):
    """
    Тестирование представления вывода данных о категориях
    """

    @classmethod
    def setUpTestData(cls):
        """
        Установка контрольных данных для проверки
        """
        cls.full_data = [{'id': 1, 'name': 'Новинки'}, {'id': 2, 'name': 'Закуски'}, {'id': 3, 'name': 'Кофе'}]

    @tag('categories')
    def test_get_categories(self):
        """
        Проверка статуса и структуры ответа при запросе категорий товаров
        """
        response = self.client.get(reverse('categories'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data, response.data)

    @tag('categories')
    def test_get_active_categories(self):
        """
        Проверка возврата только активных категорий
        """
        Category.objects.filter(id=3).update(status=False)
        response = self.client.get(reverse('categories'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data[:2], response.data)

    @tag('categories')
    def test_get_categories_with_active_products(self):
        """
        Проверка возврата категорий только с активными товарами
        """
        Product.objects.filter(id=1).update(status=False)
        response = self.client.get(reverse('categories'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data[:2], response.data)

    @tag('categories')
    def test_get_categories_with_active_variations(self):
        """
        Проверка возврата категорий только с товарами с активными вариациями
        """
        Variation.objects.filter(id=1).update(status=False)
        response = self.client.get(reverse('categories'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data[:2], response.data)
