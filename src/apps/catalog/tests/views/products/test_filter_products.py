import copy

from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.catalog.models import Product
from apps.catalog.tests.base import TestBase
from apps.catalog.tests.views.responces_data.filter_products import all_products


class TestProductsFilterListView(TestBase):
    """
    Тестирование представления вывода отфильтрованных товаров
    """

    @classmethod
    def setUpTestData(cls):
        """
        Установка контрольных данных для проверки
        """
        cls.all_products = all_products

        cls.one_product = copy.deepcopy(all_products)
        cls.one_product['count'] = 1
        cls.one_product['results'] = [all_products['results'][2]]

        cls.two_product = copy.deepcopy(all_products)
        cls.two_product['count'] = 2
        cls.two_product['results'] = all_products['results'][:2]

    @tag('products')
    def test_get_products(self):
        """
        Проверка статуса и структуры ответа при запросе товаров без параметров фильтрации
        """
        response = self.client.get(reverse('products'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.all_products, response.data)

    @tag('products')
    def test_get_products_by_category(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по категории
        """
        response = self.client.get(reverse('products'), data={'category_id': 3})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_product, response.data)

    @tag('products')
    def test_get_products_by_in_have(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров в наличии
        """
        Product.objects.filter(id__in=[2, 3]).update(count=0)
        response = self.client.get(reverse('products'), data={'in_have': 'true'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_product, response.data)

    @tag('products')
    def test_get_products_by_ingredients(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по ингредиентам
        """
        response = self.client.get(reverse('products'), data={'ingredients': '1,2'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_product, response.data)

    @tag('products')
    def test_get_products_by_max_price(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по максимальной цене
        """
        response = self.client.get(reverse('products'), data={'max_price': 170})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_product, response.data)

    @tag('products')
    def test_get_products_by_min_price(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по минимальной цене
        """
        response = self.client.get(reverse('products'), data={'min_price': 200})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.two_product, response.data)

    @tag('products')
    def test_get_products_by_pagination(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по номеру страницы
        """
        response = self.client.get(reverse('products'), data={'page': 3, 'page_size': 1})

        self.one_product['count'] = 3
        self.one_product['total_pages'] = 3
        self.one_product['previous'] = 'http://testserver/api/products/?page=2&page_size=1'

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_product, response.data)

    @tag('products')
    def test_get_products_by_name(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по названию
        """
        response = self.client.get(reverse('products'), data={'search': 'капуч'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.one_product, response.data)

    @tag('products')
    def test_get_products_by_filters(self):
        """
        Проверка статуса и структуры ответа при фильтрации товаров по нескольким параметрам фильтрации
        """
        response = self.client.get(reverse('products'), data={'min_price': 200, 'page': 2, 'page_size': 1})

        self.two_product['count'] = 2
        self.two_product['total_pages'] = 2
        self.two_product['results'] = [self.two_product['results'][1]]
        self.two_product['previous'] = 'http://testserver/api/products/?min_price=200&page_size=1'

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.two_product, response.data)

    @tag('products')
    def test_get_products_by_cort(self):
        """
        Проверка статуса и структуры ответа при сортировке товаров по цене
        """
        response = self.client.get(reverse('products'), data={'sort': 'price'})
        self.all_products['results'] = self.all_products['results'][::-1]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.all_products, response.data)
