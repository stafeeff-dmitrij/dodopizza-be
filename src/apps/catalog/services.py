import logging

from django.db.models import Min, QuerySet
from django.http import QueryDict

from apps.catalog.constants import SortTypeProduct
from apps.catalog.models import Product
from apps.exceptions import InvalidDataResponseException

logger = logging.getLogger(__name__)


class ProductFilterServices:
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
    def __filter(cls, products: QuerySet[Product], params: QueryDict) -> QuerySet[Product]:
        """
        Фильтрация товаров
        @param products: товары
        @param params: параметры фильтрации
        """

        for key, value in params.items():
            if key in cls.FILTER_FIELDS and value:
                try:
                    products = products.filter(**{cls.FILTER_FIELDS[key]: value})
                except ValueError as exc:
                    logger.error(exc)

        # только активные товары с активными вариациями
        return products.filter(status=True, variations__status=True).distinct()

    @classmethod
    def __sort(cls, products: QuerySet[Product], sort_name: str | None = None) -> QuerySet[Product]:
        """
        Сортировка товаров
        @param products: товары
        @param sort_name: параметр для сортировки
        """

        if not sort_name:
            sorted_products = products.order_by('parent_category', 'order')  # сортировка по умолчанию

        elif sort_name == SortTypeProduct.PRICE:
            sorted_products = products.order_by('min_price', 'order')

        elif sort_name == SortTypeProduct.NAME:
            sorted_products = products.order_by('name', 'order')

        else:
            raise InvalidDataResponseException('Передан невалидный ключ для сортировки товаров')

        return sorted_products

    @classmethod
    def __prep_params(cls, params: QueryDict) -> QueryDict:
        """
        Подготовка параметров фильтрации
        @param params: 'сырые' параметры фильтрации и сортировки
        @return: 'подготовленные' параметры для последующего использования для фильтрации и сортировки
        """
        ingredients = params.get('ingredients')

        if ingredients:
            params['ingredients'] = ingredients.split(',')  # список id ингредиентов

        in_have = params.get('in_have', 'false').lower() == 'true'  # приводим к boolean

        if in_have:
            params['in_have'] = 1  # минимальное кол-во товара в наличии для фильтрации
        else:
            params.pop('in_have', None)

        return params

    @classmethod
    def get_products(cls, params: QueryDict) -> QuerySet[Product]:
        """
        Возврат отфильтрованных и отсортированных товаров по переданным параметрам
        @param params: параметры фильтрации и сортировки
        @return: отфильтрованные и отсортированные товары
        """

        # Фильтрация
        filter_params = params.copy()
        # отсеиваем параметры, по которым не надо фильтровать, н-р, параметры пагинации, типа сортировки
        partial_params = set(filter_params.keys()) & set(cls.FILTER_FIELDS.keys())

        products = Product.objects.annotate(min_price=Min('variations__price'))

        if partial_params:
            filter_params = cls.__prep_params(filter_params)
            products = cls.__filter(products=products, params=filter_params)

        # Сортировка
        sort_param = params.get('sort')
        sorted_products = cls.__sort(products=products, sort_name=sort_param)

        return sorted_products
