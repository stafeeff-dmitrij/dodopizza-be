from django.contrib.auth.models import User
from django.template.loader import render_to_string

from apps.services.email import EmailNotificationService


class AccessNotificationService(EmailNotificationService):
    """
    Отправка уведомлений на email при запросе доступа к сайту
    """

    SUBJECT = 'ДОДО ПИЦЦА. Запрос доступа к сайту'

    @classmethod
    def notify_admins(cls, ip: str, email: str, comment: str) -> None:
        """
        Отправка уведомления админу
        @param ip: ip пользователя, запрашивающего доступ
        @param email: email пользователя
        @param comment: комментарий
        """

        admins = User.objects.filter(is_superuser=True)

        if admins:
            emails = [admin.email for admin in admins]
            message = render_to_string('email/access/notify_admin.html', {
                'title': cls.SUBJECT,
                'ip': ip,
                'email': email,
                'comment': comment,
            })

            cls._send_msg(cls.SUBJECT, message, emails)

    @classmethod
    def notify_user(cls, email: str, period: str) -> None:
        """
        Отправка уведомления пользователю о предоставлении доступа к сайту
        @param email: email пользователя
        @param period: временный период предоставления доступа
        """

        message = render_to_string('email/access/notify_user.html', {
            'title': cls.SUBJECT,
            'period': period,
        })

        cls._send_msg(cls.SUBJECT, message, [email])
