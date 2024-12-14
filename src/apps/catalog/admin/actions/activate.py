from django.contrib import admin

from apps.catalog.utils.status import change_status_child_records


@admin.action(description='Включить записи')
def activate_records(adminmodel, request, queryset):
    """
    Смена статуса на 'Активно', включая всех дочерних записей
    """
    change_status_child_records(records=queryset, active=True)
    queryset.update(status=True)


@admin.action(description='Включить запись')
def activate_record(adminmodel, request, queryset):
    """
    Смена статуса на 'Активно'
    """
    queryset.update(status=True)
