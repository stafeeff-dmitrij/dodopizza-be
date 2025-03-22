from django.contrib import admin
from django.db.models import QuerySet
from django.utils import timezone

from apps.access.models import AccessByIP


@admin.action(description='Ограничить доступ')
def disable_access(adminmodel, request, queryset: QuerySet[AccessByIP]):
    """
    Ограничение доступа к сайту по ip
    """
    queryset.update(access_to=timezone.now(), period=None)
