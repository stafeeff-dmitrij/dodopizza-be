from django.contrib import admin, messages
from django.db.models import QuerySet

from apps.catalog.models import Category
from apps.catalog.utils.status import change_status_child_records


@admin.action(description='Включить записи (включая дочерние)')
def activate_records(adminmodel, request, queryset):
    """
    Смена статуса на 'Активно', включая всех дочерних записей
    """
    change_status_child_records(records=queryset, active=True)
    queryset.update(status=True)


@admin.action(description='Включить запись')
def activate_record(adminmodel, request, queryset: QuerySet[Category]):
    """
    Смена статуса на 'Активно'
    """

    for record in queryset:
        if record.parent and record.parent.status is False:
            messages.set_level(request, messages.ERROR)  # Меняем уровень сообщения на ERROR
            messages.add_message(
                request,
                level=messages.ERROR,
                message=f'Нельзя активировать подкатегорию "{record.name}", '
                f'если ее родительская категория "{record.parent.name}" отключена!'
            )
            return

    queryset.update(status=True)
