from django.contrib import admin

from apps.catalog.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """
    Ингредиенты
    """

    list_display = ('id', 'order', 'name', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status',)
    search_fields = ('name',)
    search_help_text = 'Поиск по названию'
    list_editable = ('order', 'status')
    ordering = ('order',)
    list_per_page = 20

    fieldsets = [
        (
            'Основное',
            {
                'fields': ('name', 'image')
            }
        ),
        (
            'Прочее',
            {
                'fields': ('order', 'status')
            }
        )
    ]
