import os

from django.test import Client
from rest_framework.test import APITestCase

from apps.catalog.tests.base import (
    CATEGORIES,
    INGREDIENTS,
    PRODUCTS,
    VARIATION_TO_INGREDIENT,
    VARIATIONS,
)
from config.settings import BASE_DIR

FIXTURES_PATH = os.path.join(BASE_DIR, 'apps', 'access', 'tests', 'fixtures')
ACCESS = os.path.join(FIXTURES_PATH, 'access.json')
USERS = os.path.join(FIXTURES_PATH, 'users.json')


class TestBase(APITestCase):

    fixtures = [ACCESS, USERS, CATEGORIES, INGREDIENTS, PRODUCTS, VARIATIONS, VARIATION_TO_INGREDIENT]

    @classmethod
    def setUpTestData(cls):
        cls.ip = '192.168.1.100'
        cls.without_access_client = Client()
        cls.without_access_client.defaults['REMOTE_ADDR'] = cls.ip

        cls.access_data = {
            'email': 'new-test@mail.com',
            'comment': 'Запрос доступа'
        }
