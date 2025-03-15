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
            # Исключаем 2 автоматических запроса Django: проверка сессии и авторизации пользователя
            if count_requests > 2:
                logger.debug(f'Запрос: {request.path}. Кол-во запросов к БД: {count_requests - 2}')
                # for count, query in enumerate(connection.queries[2:], 1):
                #     logger.warning(f'{count}: {query}')

        return response
