import os

from django.test import override_settings
from rest_framework.test import APITestCase

from config.settings import BASE_DIR

ACCESS_FIXTURES_PATH = os.path.join(BASE_DIR, 'apps', 'access', 'tests', 'fixtures')
FIXTURES_PATH = os.path.join(BASE_DIR, 'apps', 'catalog', 'tests', 'fixtures')

ACCESS = os.path.join(ACCESS_FIXTURES_PATH, 'access.json')
CATEGORIES = os.path.join(FIXTURES_PATH, 'categories.json')
INGREDIENTS = os.path.join(FIXTURES_PATH, 'ingredients.json')
VARIATIONS = os.path.join(FIXTURES_PATH, 'variations.json')
VARIATION_TO_INGREDIENT = os.path.join(FIXTURES_PATH, 'variationtoingredient.json')
PRODUCTS = os.path.join(FIXTURES_PATH, 'products.json')


# отключаем кэширование
@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}})
class TestBase(APITestCase):

    fixtures = [ACCESS, CATEGORIES, INGREDIENTS, PRODUCTS, VARIATIONS, VARIATION_TO_INGREDIENT]
