from django.contrib import admin

from apps.catalog.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Товары
    """

    list_display = ('id', 'order', 'name', 'short_description', 'count', 'all_categories', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('categories', 'status')
    search_fields = ('name',)
    search_help_text = 'Поиск по названию'
    list_editable = ('order', 'status')
    ordering = ('order',)
    list_per_page = 20

    def short_description(self, obj):
        if obj.description:
            return obj.description[:50]
        else:
            return '-'

    short_description.short_description = 'Описание'

    def all_categories(self, obj):
        """
        Все категории, к которым принадлежит товар
        """
        return ', '.join(category.name for category in obj.categories.all())

    all_categories.short_description = 'Категории'
