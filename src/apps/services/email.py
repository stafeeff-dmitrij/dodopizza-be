from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags


class EmailNotificationService:
    """
    Отправка уведомлений на email
    """

    @classmethod
    def _send_msg(cls, subject: str, message, emails: list[str]) -> None:
        """
        Отправка подготовленного письма
        @param subject: тема письма
        @param message: тело сообщения
        @param emails: список email получателей
        """
        text_content = strip_tags(message)

        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=None,
            to=emails,
        )
        email.attach_alternative(message, 'text/html')
        email.send()
