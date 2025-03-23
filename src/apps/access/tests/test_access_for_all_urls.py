from django.test import override_settings, tag
from django.urls import reverse
from rest_framework import status

from apps.access.tests.base import TestBase


# отключаем кэширование
@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}})
class TestAccessForAllUrls(TestBase):
    """
    Тестирование корректности ограничения доступа для всех URL адресов
    """

    @tag('access')
    def test_get_categories(self):
        """
        Проверка статуса ответа при запросе категорий товаров
        """
        good_response = self.client.get(reverse('categories'))
        bad_response = self.without_access_client.get(reverse('categories'))

        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('access')
    def test_get_ingredients(self):
        """
        Проверка статуса ответа при запросе ингредиентов
        """
        good_response = self.client.get(reverse('ingredients'))
        bad_response = self.without_access_client.get(reverse('ingredients'))

        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('access')
    def test_get_all_products(self):
        """
        Проверка статуса ответа при запросе всех товаров
        """
        good_response = self.client.get(reverse('all-products'))
        bad_response = self.without_access_client.get(reverse('all-products'))

        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('access')
    def test_get_filter_products(self):
        """
        Проверка статуса ответа при запросе отфильтрованных товаров
        """
        good_response = self.client.get(reverse('products'))
        bad_response = self.without_access_client.get(reverse('products'))

        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('access')
    def test_get_product(self):
        """
        Проверка статуса ответа при запросе детальной информации о товаре
        """
        good_response = self.client.get(reverse('product-detail', kwargs={'pk': 1}))
        bad_response = self.without_access_client.get(reverse('product-detail', kwargs={'pk': 1}))

        self.assertEqual(good_response.status_code, status.HTTP_200_OK)
        self.assertEqual(bad_response.status_code, status.HTTP_403_FORBIDDEN)

    @tag('access')
    def test_request_access(self):
        """
        Проверка статуса ответа при запросе доступа к сайту (на ендпоинт не распространяется ограничение по ip)
        """
        response_1 = self.client.post(reverse('access-request'), data=self.access_data, format='json')
        response_2 = self.without_access_client.post(reverse('access-request'), data=self.access_data, format='json')

        self.assertEqual(response_1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response_2.status_code, status.HTTP_204_NO_CONTENT)

    @tag('access')
    def test_get_admin(self):
        """
        Проверка статуса ответа при запросе админки (на админку не распространяется ограничение по ip)
        """

        response_1 = self.client.login(username='admin', password='admin')
        response_2 = self.without_access_client.login(username='admin', password='admin')
        self.assertTrue(response_1 and response_2)

        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.without_access_client.get('/admin/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
