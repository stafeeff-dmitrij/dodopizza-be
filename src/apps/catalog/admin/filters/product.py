from django.contrib import admin


class ProductEndedFilter(admin.SimpleListFilter):
    """
    Фильтрация по признаку того, закончился товар или нет
    """

    title = 'наличие'
    parameter_name = 'available'

    def lookups(self, request, model_admin):
        """ Варианты фильтрации """
        return (
            ('ended', 'Закончился'),
            ('available', 'В наличии'),
        )

    def queryset(self, request, queryset):
        """ Фильтрация по признаку """

        if self.value() == 'ended':
            return queryset.filter(count=0)

        if self.value() == 'available':
            return queryset.filter(count__gt=0)

        return queryset
