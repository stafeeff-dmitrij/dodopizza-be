from django.contrib import admin

from apps.catalog.admin.actions.status import activate_record, deactivate_record
from apps.catalog.models import Category
from config.settings import PROJECT_VERSION

admin.site.site_title = 'ДОДО ПИЦЦА'
admin.site.site_header = f"ДОДО ПИЦЦА (v{PROJECT_VERSION}). Административная панель"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Категории товаров
    """

    list_display = ('id', 'order', 'name', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status',)
    search_fields = ('name',)
    search_help_text = 'Поиск по названию'
    list_editable = ('order', 'status')
    ordering = ('order',)

    actions = (activate_record, deactivate_record)
