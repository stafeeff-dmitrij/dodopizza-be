from django.db import IntegrityError
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.response import Response

from apps.access.models import AccessByIP
from apps.access.serializers import AccessRequestSerializer
from apps.access.services import AccessNotificationService


@extend_schema(tags=['Доступ'])
class AccessRequestView(generics.GenericAPIView):
    """
    Запрос доступа к сайту
    """

    serializer_class = AccessRequestSerializer

    @extend_schema(
        summary='Запрос на доступ к сайту',
        request=AccessRequestSerializer,
        responses={
            status.HTTP_204_NO_CONTENT: None,
        }
    )
    def post(self, request, *args, **kwargs):
        """
        Запроса на доступ к сайту
        """
        serializer = AccessRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ip = request.META.get('REMOTE_ADDR')

        try:
            AccessByIP.objects.create(ip=ip, access_to=None, **serializer.validated_data)
        except IntegrityError:
            AccessByIP.objects.filter(ip=ip).update(access_to=None, **serializer.validated_data)

        AccessNotificationService.notify_admins(ip=ip, **serializer.validated_data)

        return Response(status=status.HTTP_204_NO_CONTENT)
