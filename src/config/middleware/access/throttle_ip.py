from django.core.cache import cache
from django.http import JsonResponse
from rest_framework import status

MAX_REQUESTS = 50
TIMEOUT = 10


def throttle_ip_middleware(get_response):
    """
    Ограничение кол-ва запросов с одного ip
    """

    def middleware(request):
        ip = request.META.get('REMOTE_ADDR')
        count = cache.get(f'ip:{ip}', 0)

        if count >= MAX_REQUESTS:
            return JsonResponse(
                {'detail': 'Превышено максимально допустимое кол-во запросов'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        cache.set(f'ip:{ip}', count + 1, TIMEOUT)

        response = get_response(request)
        return response

    return middleware
