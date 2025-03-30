from django.contrib import admin
from django.utils import timezone


class AccessFilter(admin.SimpleListFilter):
    """
    Фильтрация по наличию доступа
    """

    title = 'наличие доступа'
    parameter_name = 'access'

    def lookups(self, request, model_admin):
        """ Варианты фильтрации """
        return (
            ('allowed', 'Разрешен'),
            ('ended', 'Закончен'),
            ('queried', 'Запрошен'),
        )

    def queryset(self, request, queryset):
        """ Фильтрация по признаку """

        if self.value() == 'allowed':
            return queryset.filter(access_to__gt=timezone.now())

        if self.value() == 'ended':
            return queryset.filter(access_to__lt=timezone.now())

        if self.value() == 'queried':
            return queryset.filter(period=None, access_to=None)

        return queryset
