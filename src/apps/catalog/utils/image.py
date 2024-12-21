import os

PRODUCT_PATH = os.path.join('apps', 'catalog', 'static', 'catalog', 'images', 'variation')


def get_variation_image_path(instance, filename: str) -> str:
    """
    Возврат ссылки для сохранения изображения вариации товара
    :param instance: товар
    :param filename: название файла
    :return: директория для сохранения картинки
    """
    return os.path.join(
        PRODUCT_PATH, f'{instance.id}', filename
    )
