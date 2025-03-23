from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from django.test import tag
from django.urls import reverse

from apps.access.constants import AccessPeriodChoice
from apps.access.models import AccessByIP
from apps.access.services import AccessNotificationService
from apps.access.tests.base import TestBase


class TestSendEmails(TestBase):
    """
    Тестирование отправки email
    """

    @tag('emails')
    def test_notify_admins(self):
        """
        Проверка отправки email админу при получении нового запроса на доступ к сайту
        """
        self.without_access_client.post(reverse('access-request'), data=self.access_data, format='json')
        admin = User.objects.get(username='admin')

        # Проверяем, что письмо отправлено
        self.assertEqual(len(mail.outbox), 1)

        # Проверяем содержимое, кому и откуда отправился email
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, AccessNotificationService.SUBJECT)
        self.assertEqual(sent_email.from_email, settings.EMAIL_HOST_USER)
        self.assertEqual(sent_email.to, [admin.email])

        self.assertEqual(sent_email.alternatives[0][1], 'text/html')

    @tag('emails')
    def test_notify_user(self):
        """
        Проверка отправки email пользователю при выдаче доступа к сайту
        """
        access = AccessByIP.objects.get(ip='127.0.0.1')
        access.period = AccessPeriodChoice.TEN_MIN
        access.access_to = None
        access.save()

        # Проверяем, что письмо отправлено
        self.assertEqual(len(mail.outbox), 1)

        # Проверяем содержимое, кому и откуда отправился email
        sent_email = mail.outbox[0]
        self.assertEqual(sent_email.subject, AccessNotificationService.SUBJECT)
        self.assertEqual(sent_email.from_email, settings.EMAIL_HOST_USER)
        self.assertEqual(sent_email.to, [access.email])

        self.assertEqual(sent_email.alternatives[0][1], 'text/html')
