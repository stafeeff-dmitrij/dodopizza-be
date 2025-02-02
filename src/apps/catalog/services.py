import logging

from django.db.models import Min, QuerySet
from django.http import QueryDict

from apps.catalog.constants import SortTypeProduct
from apps.catalog.models import Product
from apps.catalog.utils.filter import get_partial_match
from apps.exceptions import InvalidDataResponseException

logger = logging.getLogger(__name__)


class FilterAndSortProductServices:
    """
    Фильтрация товаров по переданным параметрам
    """

    FILTER_FIELDS = {
        'category_id': 'categories__id',
        'search': 'name__icontains',
        'ingredients': 'variations__ingredients__id__in',
        'min_price': 'min_price__gte',  # поле min_price добавлено через annotate!
        'max_price': 'min_price__lte',  # поле min_price добавлено через annotate!
        'in_have': 'count__gt'
    }

    @classmethod
    def filter(cls, params: QueryDict) -> QuerySet[Product]:
        """
        Фильтрация товаров
        """

        products = Product.objects.prefetch_related('variations').annotate(min_price=Min('variations__price'))

        for key, value in params.items():
            if key in cls.FILTER_FIELDS and value:
                try:
                    products = products.filter(**{cls.FILTER_FIELDS[key]: value})
                except ValueError as exc:
                    logger.error(exc)

        return products.filter(status=True).distinct()

    @classmethod
    def sort(cls, products: QuerySet[Product], sort_name: str = None) -> QuerySet[Product]:
        """
        Сортировка товаров
        """

        if not sort_name:
            sorted_products = products.order_by('parent_category', 'order')  # сортировка по умолчанию

        elif sort_name == SortTypeProduct.PRICE:
            sorted_products = products.annotate(min_price=Min('variations__price')).order_by('min_price', 'order')

        elif sort_name == SortTypeProduct.NAME:
            sorted_products = products.order_by('name', 'order')

        else:
            raise InvalidDataResponseException('Передан невалидный ключ для сортировки товаров')

        return sorted_products

    @classmethod
    def get_products(cls, params: QueryDict) -> QuerySet[Product]:
        """
        Возврат отфильтрованных и отсортированных товаров по переданным параметрам
        """

        # Фильтрация
        filter_params = params.copy()
        partial_params = get_partial_match(filter_params, cls.FILTER_FIELDS)

        if partial_params:
            ingredients = filter_params.get('ingredients')

            if ingredients:
                filter_params['ingredients'] = ingredients.split(',')  # список id ингредиентов

            in_have = filter_params.get('in_have', 'false').lower() == 'true'  # приводим к boolean

            if in_have:
                filter_params['in_have'] = 1  # минимальное кол-во товара в наличии для фильтрации
            else:
                filter_params.pop('in_have', None)

            products = FilterAndSortProductServices.filter(params=filter_params)
        else:
            products = Product.objects.prefetch_related('variations').all()

        # Сортировка
        sort_param = params.get('sort')
        sorted_products = FilterAndSortProductServices.sort(products=products, sort_name=sort_param)

        return sorted_products
