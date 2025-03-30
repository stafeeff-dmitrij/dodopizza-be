from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.catalog.models import Product, Variation
from apps.catalog.tests.base import TestBase
from apps.catalog.tests.views.responces_data.all_products import all_products


class TestAllProductsListView(TestBase):
    """
    Тестирование представления вывода товаров для главной страницы
    """

    @classmethod
    def setUpTestData(cls):
        """
        Установка контрольных данных для проверки
        """
        cls.full_data = all_products

    @tag('products')
    def test_get_products(self):
        """
        Проверка статуса и структуры ответа при запросе товаров
        """
        response = self.client.get(reverse('all-products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data, response.data)

    @tag('products')
    def test_get_active_products(self):
        """
        Проверка возврата только активных товаров
        """
        Product.objects.filter(id=1).update(status=False)
        response = self.client.get(reverse('all-products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data[:-1], response.data)

    @tag('products')
    def test_get_products_with_active_variations(self):
        """
        Проверка возврата товаров только с активными вариациями
        """
        Variation.objects.filter(id=1).update(status=False)
        response = self.client.get(reverse('all-products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data[:-1], response.data)

    @tag('products')
    def test_sorting_products(self):
        """
        Проверка сортировки при выводе товаров
        """
        Product.objects.filter(id=2).update(order=3)
        Product.objects.filter(id=3).update(order=2)

        updated_products = self.full_data[1]['products'][::-1]
        self.full_data[1]['products'] = updated_products

        response = self.client.get(reverse('all-products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data, response.data)
