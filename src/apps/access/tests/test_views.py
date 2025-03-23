from django.test import override_settings, tag
from django.urls import reverse
from rest_framework import status

from apps.access.models import AccessByIP
from apps.access.tests.base import TestBase


# отключаем кэширование
@override_settings(CACHES={'default': {'BACKEND': 'django.core.cache.backends.dummy.DummyCache'}})
class TestAccessRequestView(TestBase):
    """
    Тестирование представлений
    """

    @tag('views')
    def test_create_access(self):
        """
        Проверка создания новой записи при запросе доступа
        """
        response = self.without_access_client.post(reverse('access-request'), data=self.access_data, format='json')
        new_rec = AccessByIP.objects.get(ip=self.ip)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(new_rec.email, self.access_data['email'])
        self.assertEqual(new_rec.comment, self.access_data['comment'])

    @tag('views')
    def test_update_access(self):
        """
        Проверка обновления существующей записи при запросе доступа
        """
        response = self.client.post(reverse('access-request'), data=self.access_data, format='json')
        new_rec = AccessByIP.objects.get(ip='127.0.0.1')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(new_rec.email, self.access_data['email'])
        self.assertEqual(new_rec.comment, self.access_data['comment'])
