from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.catalog.models import Ingredient
from apps.catalog.tests.base import TestBase


class TestIngredientsListView(TestBase):
    """
    Тестирование представления вывода данных об ингредиентах
    """

    @classmethod
    def setUpTestData(cls):
        """
        Установка контрольных данных для проверки
        """
        cls.full_data = [
            {'id': 1, 'name': 'Сироп со вкусом яблочного пирога'},
            {'id': 2, 'name': 'Кокосовый сироп'},
        ]

    @tag('ingredients')
    def test_get_ingredients(self):
        """
        Проверка статуса и структуры ответа при запросе ингредиентов
        """
        response = self.client.get(reverse('ingredients'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data[:1], response.data)

    @tag('ingredients')
    def test_get_filter_ingredients(self):
        """
        Проверка возврата ингредиентов, отфильтрованных по категории
        """
        response = self.client.get(reverse('ingredients'), data={'category_id': 3})
        self.assertEqual(self.full_data[:1], response.data)

        response = self.client.get(reverse('ingredients'), data={'category_id': 1})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([], response.data)

    @tag('ingredients')
    def test_sorting_ingredients(self):
        """
        Проверка сортировки при выводе ингредиентов
        """
        Ingredient.objects.filter(id=2).update(status=True)
        response = self.client.get(reverse('ingredients'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.full_data, response.data)
