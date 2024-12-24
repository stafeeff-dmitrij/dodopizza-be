from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CatalogPagination(PageNumberPagination):
    """
    Пагинация для каталога товаров (с общим кол-вом страниц)
    """

    page_size = 12
    max_page_size = 30

    def get_paginated_response(self, data):
        total_count = self.page.paginator.count
        page_size = self.page_size
        total_pages = (total_count + page_size - 1) // page_size

        return Response({
            'count': total_count,
            'total_pages': total_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data,
        })
