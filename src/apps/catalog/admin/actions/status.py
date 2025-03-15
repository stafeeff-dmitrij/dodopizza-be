from django.contrib import admin
from django.db.models import QuerySet


@admin.action(description='Установить статус "Активно"')
def activate_record(adminmodel, request, queryset: QuerySet):
    """
    Смена статуса на 'Активно'
    """
    queryset.update(status=True)


@admin.action(description='Установить статус "Не активно"')
def deactivate_record(adminmodel, request, queryset: QuerySet):
    """
    Смена статуса на 'Не активно'
    """
    queryset.update(status=False)
