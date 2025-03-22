from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.access.models import AccessByIP
from apps.access.services import AccessNotificationService


@receiver(post_save, sender=AccessByIP)
def notification_of_access(sender, instance: AccessByIP, created, **kwargs):
    """
    Уведомление о получении доступа к сайту
    """

    if instance.period and not instance.access_to:
        AccessNotificationService.notify_user(
            email=instance.email,
            period=instance.get_period_display()
        )
