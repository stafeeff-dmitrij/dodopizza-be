from django.contrib import admin


class ParentCategoryFilter(admin.SimpleListFilter):
    """
    Фильтрация по признаку категорий 'родительская' / 'дочерняя запись'
    """

    title = 'категория'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        """ Варианты фильтрации """
        return (
            ('parent', 'Главные'),
            ('not_parent', 'Подкатегории'),
        )

    def queryset(self, request, queryset):
        """ Фильтрация по признаку """

        if self.value() == 'parent':
            return queryset.filter(parent=None)

        if self.value() == 'not_parent':
            return queryset.exclude(parent=None)

        return queryset
