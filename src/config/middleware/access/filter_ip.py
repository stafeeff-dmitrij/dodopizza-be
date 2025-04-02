import logging

from django.http import JsonResponse
from django.utils import timezone
from rest_framework import status

from apps.access.models import AccessByIP
from apps.access.utils import get_access_to

logger = logging.getLogger(__name__)


ALLOWED_URL = (
    '/admin/',
    '/media/',
    '/api/access/request/',
)


class FilterIPMiddleware:
    """
    Ограничение доступа по ip
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        logger.info(f'ip: {ip}')
        record = AccessByIP.objects.filter(ip=ip).first()

        if (not record or record.access_to and record.access_to <= timezone.now()) and not any(request.path.startswith(url) for url in ALLOWED_URL):
            return JsonResponse(
                {'detail': 'Доступ ограничен'},
                status=status.HTTP_403_FORBIDDEN,
                json_dumps_params={'ensure_ascii': False}
            )

        # доступ предоставлен, заходит в первый раз
        # сохраняем время, до которого разрешен доступ, начиная таким образом обратный отсчет
        if record and record.period and not record.access_to:
            record.access_to = get_access_to(access_period=record.period)
            record.save()

        response = self.get_response(request)
        return response
