from django.contrib import admin

from apps.catalog.admin.actions import activate_record
from apps.catalog.admin.actions.status import deactivate_record
from apps.catalog.admin.filters.product import ProductEndedFilter
from apps.catalog.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Товары
    """

    list_display = ('id', 'name', 'short_description', 'count', 'parent_category',
                    'all_categories', 'default_ingredients', 'order', 'status')
    list_display_links = ('name',)
    list_filter = ('parent_category', 'categories', 'status', ProductEndedFilter)
    search_fields = ('name',)
    search_help_text = 'Поиск по названию'
    list_editable = ('order', 'status')
    ordering = ('parent_category', 'order')
    filter_horizontal = ('categories', 'ingredients',)
    list_per_page = 20

    actions = (activate_record, deactivate_record)

    @admin.display(description='Описание')
    def short_description(self, obj):
        if obj.description:
            return obj.description[:50]
        else:
            return '-'

    @admin.display(description='Категории')
    def all_categories(self, obj):
        """
        Все категории, к которым принадлежит товар
        """
        return ', '.join(category.name for category in obj.categories.all())

    @admin.display(description='Ингредиенты по умолчанию')
    def default_ingredients(self, obj):
        """
        Ингредиенты по умолчанию
        """
        return ', '.join(ingredient.name for ingredient in obj.ingredients.all())

    fieldsets = [
        (
            'Основное',
            {
                'fields': ('name', 'description', 'count', 'parent_category', 'categories')
            }
        ),
        (
            'Доп.параметры',
            {
                'fields': ('ingredients',)
            }
        ),
        (
            'Прочее',
            {
                'fields': ('order', 'status')
            }
        )
    ]
