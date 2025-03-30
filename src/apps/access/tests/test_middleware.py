from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.access.constants import AccessPeriodChoice
from apps.access.models import AccessByIP
from apps.access.tests.base import TestBase
from apps.access.utils import get_access_to


class TestMiddleware(TestBase):
    """
    Тестирование middleware
    """

    @tag('middleware')
    def test_filter_ip(self):
        """
        Проверка сохранения времени доступа при первом посещении с разрешенного ip
        """

        AccessByIP.objects.create(
            ip=self.ip,
            email='test@mail.ru',
            comment='Тест',
            period=AccessPeriodChoice.TEN_MIN
        )

        response = self.without_access_client.get(reverse('categories'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        check_record = AccessByIP.objects.get(ip=self.ip)
        control_data = get_access_to(access_period=AccessPeriodChoice.TEN_MIN)
        self.assertEqual(control_data.replace(microsecond=0), check_record.access_to.replace(microsecond=0))

    @tag('middleware')
    def test_filter_ip_for_admin(self):
        """
        Проверка доступности админки
        """
        response = self.client.get(reverse('admin:login'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
