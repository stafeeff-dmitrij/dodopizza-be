import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatalogPagination(PageNumberPagination):
    """
    Пагинация для каталога товаров (с общим кол-вом страниц)
    """

    page_size = 12
    page_query_param = 'page'
    page_query_description = 'Номер страницы'
    page_size_query_param = 'page_size'
    page_size_query_description = 'Кол-во записей на странице'
    max_page_size = 30

    def get_paginated_response(self, data):
        total_count = self.page.paginator.count
        page_size = self.get_page_size(self.request) or self.page_size
        total_pages = math.ceil(total_count / page_size)

        return Response({
            'count': total_count,
            'total_pages': total_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
