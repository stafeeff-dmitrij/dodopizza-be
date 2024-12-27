import os

IMAGES_PATH = os.path.join('apps', 'catalog', 'static', 'catalog', 'images')


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
