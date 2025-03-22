from django.core.cache import cache
from django.http import JsonResponse
from rest_framework import status


def throttle_ip_middleware(get_response):
    """
    Ограничение кол-ва запросов с одного ip
    """

    def middleware(request):
        max_requests = 50
        timeout = 10

        ip = request.META.get('REMOTE_ADDR')
        count = cache.get(f'ip:{ip}', 0)

        if count >= max_requests:
            return JsonResponse(
                {'detail': 'Превышено максимально допустимое кол-во запросов'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )

        cache.set(f'ip:{ip}', count + 1, timeout)

        response = get_response(request)
        return response

    return middleware
