import os

from django.conf import settings

IMAGES_PATH = os.path.join('apps', 'catalog', 'static', 'catalog', 'images')
HOST = f'{settings.HTTP_PROTOCOL}://{settings.HOST}:{settings.PORT}'


def get_variation_image_path(instance, filename: str) -> str:
    """
    Возврат ссылки для сохранения изображения вариации товара
    :param instance: товар
    :param filename: название файла
    :return: директория для сохранения картинки
    """
    return os.path.join(
        IMAGES_PATH, 'variations', filename
    )


def get_ingredient_image_path(instance, filename: str) -> str:
    """
    Возврат ссылки для сохранения изображения ингредиента
    :param instance: ингредиент
    :param filename: название файла
    :return: директория для сохранения картинки
    """
    return os.path.join(
        IMAGES_PATH, 'ingredients', filename
    )


def get_url_image(image_path: str) -> str:
    """
    Возврат полного URL-адреса изображения.
    @param image_path: URL изображения, переданный через ImageField().url
    """
    return f'{HOST}{image_path}'


def get_url_str_image(image_path: str) -> str:
    """
    Возврат полного URL-адреса изображения.
    @param image_path: URL изображения
    """
    return f'{HOST}{settings.MEDIA_URL}{image_path}'
