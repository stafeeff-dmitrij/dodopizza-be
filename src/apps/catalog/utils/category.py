from apps.catalog.models import Category


def check_max_level_category(category: Category, parent: bool = False) -> bool:
    """
    Проверка максимального уровня вложенности категории

    :param category: категория
    :param parent: обозначение родительской категории или дочерней
    :return: True - уровень вложенности 1 или 2, иначе False
    """

    max_indent = 1 if parent else 2
    lvl = category.parent.level + 1

    if lvl >= max_indent:
        return False
    return True
