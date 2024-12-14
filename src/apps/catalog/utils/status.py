from apps.catalog.models import Category


def change_status_child_records(records: list[Category], active: bool) -> None:
    """
    Включение / отключение дочерних записей (смена статуса на 'Активно' / 'Не активно')
    @param records: категории товаров
    @param active: флаг для активации или деактивации записей
    """

    deleted_objects = []

    for record in records:
        children = record.get_descendants(include_self=False)  # Получаем все дочерние записи

        for child in children:
            child.status = True if active else False
            deleted_objects.append(child)

    Category.objects.bulk_update(deleted_objects, ['status'])
