from django.contrib import admin
from django.db.models import QuerySet

from apps.catalog.models import Category


@admin.action(description='Включить запись')
def activate_record(adminmodel, request, queryset: QuerySet[Category]):
    """
    Смена статуса на 'Активно'
    """
    queryset.update(status=True)


@admin.action(description='Отключить запись')
def deactivate_record(adminmodel, request, queryset):
    """
    Смена статуса на 'Не активно'
    """
    queryset.update(status=False)
