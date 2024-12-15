from django.contrib import admin

from apps.catalog.utils.status import change_status_child_records


@admin.action(description='Отключить записи (включая дочерние)')
def deactivate_records(adminmodel, request, queryset):
    """
    Смена статуса на 'Не активно', включая всех дочерних записей
    """
    change_status_child_records(records=queryset, active=False)
    queryset.update(status=False)


@admin.action(description='Отключить запись')
def deactivate_record(adminmodel, request, queryset):
    """
    Смена статуса на 'Не активно'
    """
    queryset.update(status=False)
