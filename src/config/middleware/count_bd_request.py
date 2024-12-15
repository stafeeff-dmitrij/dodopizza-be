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
            logger.debug(f'Запрос: {request.path}. Кол-во запросов к БД: {len(connection.queries)}')
            # logger.debug(f'Запросы к БД: {connection.queries}')

        return response
