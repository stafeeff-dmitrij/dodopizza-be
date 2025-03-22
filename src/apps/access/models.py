from django.db import models

from apps.access.constants import AccessPeriodChoice


class AccessByIP(models.Model):
    """
    Доступ к сайту по ip адресу
    """

    ip = models.GenericIPAddressField(primary_key=True, verbose_name='ip адрес')
    email = models.EmailField(verbose_name='email')
    comment = models.TextField(verbose_name='комментарий')

    period = models.CharField(choices=AccessPeriodChoice, verbose_name='период доступа', blank=True, null=True)
    access_to = models.DateTimeField(verbose_name='доступ до', blank=True, null=True)

    class Meta:
        db_table = 'access_by_ip'
        verbose_name = 'Доступ по IP'
        verbose_name_plural = 'Доступ по IP'

    def __str__(self) -> str:
        return f'ip: {self.ip}, email: {self.email}'
