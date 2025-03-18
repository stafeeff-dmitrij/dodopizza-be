from django.contrib import admin

from apps.catalog.admin.actions import activate_record
from apps.catalog.admin.actions.status import deactivate_record
from apps.catalog.models import Variation, VariationToIngredient


class VariationToIngredientInline(admin.TabularInline):
    """
    Привязка ингредиентов к вариации товара с ценой
    """
    model = VariationToIngredient
    extra = 0
    ordering = ('order',)
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Ингредиенты'


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    """
    Вариации товаров
    """

    list_display = ('id', 'product', 'pizza_size', 'pizza_type', 'count', 'portion_size',
                    'volume', 'weight', 'mass', 'price', 'ingredients_count', 'order', 'status')
    list_display_links = ('product',)
    list_filter = ('product__parent_category', 'product__categories', 'pizza_size',
                   'pizza_type', 'count', 'portion_size', 'volume', 'weight', 'status')
    search_fields = ('product__name',)
    search_help_text = 'Поиск по названию товара'
    list_editable = ('order', 'status')
    ordering = ('product__parent_category', 'product', 'order')
    list_per_page = 20

    actions = (activate_record, deactivate_record)

    fieldsets = [
        (
            'Основное',
            {
                'fields': ('product', 'image', 'mass', 'price')
            }
        ),
        (
            'Доп.параметры',
            {
                'fields': ('pizza_size', 'pizza_type', 'count', 'portion_size', 'volume', 'weight')
            }
        ),
        (
            'Прочее',
            {
                'fields': ('order', 'status')
            }
        )
    ]

    inlines = [VariationToIngredientInline]

    @admin.display(description='Ингредиенты')
    def ingredients_count(self, obj) -> int | str:
        """
        Кол-во ингредиентов
        """
        ingredients_count = obj.ingredients.all().count()
        return ingredients_count if ingredients_count else '-'
