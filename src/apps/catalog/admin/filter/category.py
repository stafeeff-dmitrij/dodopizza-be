from django.contrib import admin


class ParentCategoryFilter(admin.SimpleListFilter):
    """
    Фильтрация по признаку категорий 'родительская' / 'дочерняя запись'
    """

    title = 'тип категории'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        """ Варианты фильтрации """
        return (
            ('parent', 'Главная'),
            ('child', 'Подкатегория'),
        )

    def queryset(self, request, queryset):
        """ Фильтрация по признаку """

        if self.value() == 'parent':
            return queryset.filter(parent=None)

        if self.value() == 'child':
            return queryset.exclude(parent=None)

        return queryset
