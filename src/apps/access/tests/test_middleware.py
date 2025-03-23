import time
from datetime import datetime

from django.test import tag
from django.urls import reverse
from rest_framework import status

from apps.access.constants import AccessPeriodChoice
from apps.access.models import AccessByIP
from apps.access.tests.base import TestBase
from apps.access.utils import get_access_to
from config.middleware.access.throttle_ip import MAX_REQUESTS


def recurring_requests(self):
    """
    Повторяющиеся запросы для проверки ограничения при превышении максимально допустимого кол-ва запросов
    """
    start_time = datetime.now()

    for i in range(1, MAX_REQUESTS + 2):
        response = self.client.get(reverse('categories'))
        pass_sec = abs(datetime.now() - start_time).total_seconds()

        if pass_sec <= 10:
            if i <= MAX_REQUESTS:
                self.assertEqual(response.status_code, status.HTTP_200_OK)
            else:
                self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)


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
    def test_throttle_ip(self):
        """
        Проверка ограничения кол-ва запросов с одного ip
        """
        recurring_requests(self)
        time.sleep(10)
        recurring_requests(self)  # проверка сброса ограничения через допустимый интервал времени
