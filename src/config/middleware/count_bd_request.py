import logging

from django.conf import settings
from django.db import connection
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class CheckCountDbRequestMiddleware(MiddlewareMixin):
    """
    Проверка и вывод кол-во совершаемых запросов к БД
    """

    def process_response(self, request, response):
        if settings.DEBUG and request.resolver_match and request.resolver_match.url_name not in ['schema', 'swagger-ui']:
            count_requests = len(connection.queries)
            if count_requests > 0:
                logger.debug(f'Запрос: {request.path}. Кол-во запросов к БД: {count_requests}')
                # logger.debug(f'Запросы к БД: {connection.queries}')

        return response
