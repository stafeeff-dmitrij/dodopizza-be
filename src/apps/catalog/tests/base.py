import os

from django.test import override_settings
from rest_framework.test import APITestCase

from config.settings import BASE_DIR

FIXTURES_PATH = os.path.join(BASE_DIR, 'apps', 'catalog', 'tests', 'fixtures')

CATEGORIES = os.path.join(FIXTURES_PATH, 'categories.json')
INGREDIENTS = os.path.join(FIXTURES_PATH, 'ingredients.json')
VARIATIONS = os.path.join(FIXTURES_PATH, 'variations.json')
VARIATION_TO_INGREDIENT = os.path.join(FIXTURES_PATH, 'variationtoingredient.json')
PRODUCTS = os.path.join(FIXTURES_PATH, 'products.json')


# отключаем кэширование
@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}})
class TestBase(APITestCase):

    fixtures = [CATEGORIES, INGREDIENTS, PRODUCTS, VARIATIONS, VARIATION_TO_INGREDIENT]
