from django.db.models import (
    Case,
    ImageField,
    Min,
    OuterRef,
    Prefetch,
    Q,
    QuerySet,
    Subquery,
    When,
)

from apps.catalog.constants import CategoryType, PizzaSizeChoice, PizzaTypeChoice
from apps.catalog.models import (
    Category,
    Ingredient,
    Product,
    Variation,
    VariationToIngredient,
)

# подзапросы на получение нужного изображения
subq_pizza_img = Variation.objects.filter(
    product_id=OuterRef('id'),
    pizza_size=PizzaSizeChoice.average,
    pizza_type=PizzaTypeChoice.traditional
)[:1].values('image')

subq_product_img = Variation.objects.filter(
    product_id=OuterRef('id'),
)[:1].values('image')


# оптимизация кол-ва запросов к БД с 360 до 3 для главной страницы!
def get_all_product_queryset() -> QuerySet[Product]:
    """
    Возврат оптимизированного Queryset-объекта со всеми товарами
    """

    return (
        Category.objects
        .prefetch_related(
            Prefetch(
                'products',
                queryset=Product.objects.annotate(
                    min_price=Min('variations__price'),  # минимальная цена среди всех вариаций товара
                    # изображение средней пиццы либо первой вариации для других категорий товаров
                    image=Case(
                        # в зависимости от категории текущего товара извлекаем нужную картинку подзапросом
                        When(parent_category_id=CategoryType.pizza, then=Subquery(subq_pizza_img)),
                        When(~Q(parent_category_id=CategoryType.pizza), then=Subquery(subq_product_img)),
                        output_field=ImageField()
                    )
                ).filter(status=True, variations__status=True).order_by('order')),
            Prefetch('products__variations', queryset=Variation.objects.order_by('order')),
            # активные категории с активными товарами с активными вариациями
        ).filter(status=True, products__status=True, products__variations__status=True).distinct().order_by('order')
    )


# с учетом пагинации оптимизация кол-ва запросов к БД с 36 до 3 для отфильтрованных товаров!
def get_filter_product_queryset(queryset: QuerySet[Product]) -> QuerySet[Product]:
    """
    Возврат оптимизированного Queryset-объекта с отфильтрованными товарами
    """

    return (
        queryset
        .prefetch_related(Prefetch('variations', queryset=Variation.objects.order_by('order')))
        .annotate(
            image=Case(
                When(parent_category_id=CategoryType.pizza, then=Subquery(subq_pizza_img)),
                When(~Q(parent_category_id=CategoryType.pizza), then=Subquery(subq_product_img)),
                output_field=ImageField()
            ))
    )

# оптимизация кол-ва запросов к БД с 105 до 4 для страницы товара!


def get_product_detail_queryset() -> QuerySet[Product]:
    """
    Возврат оптимизированного Queryset-объекта с детальной информацией о товаре
    """

    return (Product.objects.filter(status=True, variations__status=True).distinct()
            .prefetch_related(
            Prefetch('ingredients', queryset=Ingredient.objects.filter(
                status=True).order_by('order').only('id', 'name')),
            Prefetch('variations', queryset=Variation.objects.filter(status=True).order_by('order')),
            Prefetch('variations__ingredients', queryset=VariationToIngredient.objects.select_related('ingredient').filter(
                ingredient__status=True).order_by('order')),
            ))
