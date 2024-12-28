from django.contrib import admin

from apps.catalog.models import Variation, VariationToIngredient


class VariationToIngredientInline(admin.TabularInline):
    """
    Привязка ингредиентов к вариации товара с ценой
    """
    model = VariationToIngredient
    extra = 0
    verbose_name = 'Ингредиент'
    verbose_name_plural = 'Ингредиенты'


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    """
    Вариации товаров
    """

    list_display = ('id', 'order', 'product', 'pizza_size', 'pizza_type', 'count', 'portion_size',
                    'volume', 'weight', 'mass', 'price', 'ingredients_count', 'status')
    list_display_links = ('id', 'product')
    list_filter = ('product__categories', 'pizza_size', 'pizza_type', 'count', 'portion_size', 'volume', 'weight')
    search_fields = ('product__name',)
    search_help_text = 'Поиск по названию товара'
    list_editable = ('order', 'status')
    ordering = ('order',)
    list_per_page = 20

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

    def ingredients_count(self, obj):
        """
        Кол-во ингредиентов
        """
        return obj.ingredients.all().count()

    ingredients_count.short_description = 'Ингредиенты'
