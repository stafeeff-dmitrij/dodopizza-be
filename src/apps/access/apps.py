from django.apps import AppConfig


class AccessConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.access'
    verbose_name = 'Доступ'

    def ready(self):
        # подключение сигналов
        import apps.access.signals  # noqa
