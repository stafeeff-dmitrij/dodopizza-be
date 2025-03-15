from django.contrib import admin

from apps.catalog.admin.actions import activate_record
from apps.catalog.admin.actions.status import deactivate_record
from apps.catalog.models import Ingredient


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """
    Ингредиенты
    """

    list_display = ('id', 'name', 'category', 'order', 'status')
    list_display_links = ('name',)
    list_filter = ('category', 'status')
    search_fields = ('name',)
    search_help_text = 'Поиск по названию'
    list_editable = ('order', 'status')
    ordering = ('order',)
    list_per_page = 20

    actions = (activate_record, deactivate_record)

    fieldsets = [
        (
            'Основное',
            {
                'fields': ('name', 'category', 'image')
            }
        ),
        (
            'Прочее',
            {
                'fields': ('order', 'status')
            }
        )
    ]
