from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.catalog.models import Ingredient, Product, Variation
from apps.catalog.tests.base import TestBase
from apps.catalog.tests.views.responces_data.detail_product import (
    detail_product,
    product_without_ingredients,
)


class TestProductDetailView(TestBase):
    """
    Тестирование представления вывода детальной информации о товаре
    """

    @classmethod
    def setUpTestData(cls):
        """
        Установка контрольных данных для проверки
        """
        cls.full_data = detail_product
        cls.without_ingredients = product_without_ingredients

    @tag('products')
    def test_get_product(self):
        """
        Проверка статуса и структуры ответа при запросе данных о товаре
        """
        response = self.client.get(reverse('product-detail', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data, response.data)

    @tag('products')
    def test_get_inactive_product(self):
        """
        Проверка статуса ответа при запросе данных о неактивном товаре
        """
        Product.objects.filter(id=2).update(status=False)
        response = self.client.get(reverse('product-detail', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @tag('products')
    def test_get_product_with_inactive_variations(self):
        """
        Проверка статуса ответа при запросе товара с неактивными вариациями
        """
        Variation.objects.filter(product_id=2).update(status=False)
        response = self.client.get(reverse('product-detail', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    @tag('products')
    def test_get_product_with_inactive_ingredients(self):
        """
        Проверка ответа при запросе товара с неактивными ингредиентами
        """
        Ingredient.objects.filter(category_id=3).update(status=False)
        response = self.client.get(reverse('product-detail', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.without_ingredients, response.data)

    @tag('products')
    def test_sorting_variations(self):
        """
        Проверка сортировки вариаций при выводе товара
        """
        Variation.objects.filter(id=2).update(order=2)
        Variation.objects.filter(id=3).update(order=1)

        updated_variations = self.full_data['variations'][::-1]
        self.full_data['variations'] = updated_variations

        response = self.client.get(reverse('product-detail', kwargs={'pk': 2}))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data, response.data)
