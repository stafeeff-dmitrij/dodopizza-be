import os

from django.conf import settings
from django.test import TestCase, tag

from apps.catalog.utils import get_variation_image_path
from apps.catalog.utils.image import (
    HOST,
    IMAGES_PATH,
    get_ingredient_image_path,
    get_url_image,
    get_url_str_image,
)


class TestUtils(TestCase):
    """
    Тестирование утилит
    """

    @classmethod
    def setUpTestData(cls):
        cls.file_name = 'test_image.jpg'
        cls.file_path = f'/media/{cls.file_name}'

    @tag('utils')
    def test_variation_image_path(self):
        """
        Проверка создания ссылки для сохранения изображения вариации товара
        """
        image_path = get_variation_image_path(instance=object, filename=self.file_name)
        control_res = os.path.join(IMAGES_PATH, 'variations', self.file_name)

        self.assertEqual(control_res, image_path)

    @tag('utils')
    def test_ingredient_image_path(self):
        """
        Проверка создания ссылки для сохранения изображения ингредиента
        """
        image_path = get_ingredient_image_path(instance=object, filename=self.file_name)
        control_res = os.path.join(IMAGES_PATH, 'ingredients', self.file_name)

        self.assertEqual(control_res, image_path)

    @tag('utils')
    def test_url_image(self):
        """
        Проверка возврата полного URL-адреса изображения (для ImageField().url)
        """
        image_path = get_url_image(image_path=self.file_path)
        control_res = f'{HOST}{self.file_path}'

        self.assertEqual(control_res, image_path)

    @tag('utils')
    def test_url_str_image(self):
        """
        Проверка возврата полного URL-адреса изображения
        """
        image_path = get_url_str_image(image_path=self.file_name)
        control_res = f'{HOST}{settings.MEDIA_URL}{self.file_name}'

        self.assertEqual(control_res, image_path)
