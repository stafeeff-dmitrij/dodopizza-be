from django.contrib import admin
from django.utils import timezone

from apps.access.admin.actions import disable_access
from apps.access.admin.filters import AccessFilter
from apps.access.models import AccessByIP


@admin.register(AccessByIP)
class AccessByIPAdmin(admin.ModelAdmin):
    """
    Доступ к сайту по ip
    """

    list_display = ('ip', 'email', 'comment', 'period', 'access_to', 'access')
    list_display_links = ('ip', 'email')
    readonly_fields = ('access_to',)
    search_fields = ('ip', 'email')
    search_help_text = 'Поиск по ip / email'
    actions = (disable_access,)
    list_filter = (AccessFilter,)
    list_per_page = 20

    @admin.display(description='Доступ', boolean=True)
    def access(self, obj):
        if obj.access_to and obj.access_to > timezone.now():
            return True
        return False

    def save_model(self, request, obj, form, change):
        """
        Сброс 'Доступ до' при редактировании периода доступа
        """
        current_obj = AccessByIP.objects.filter(pk=obj.pk).first()

        if current_obj and current_obj.period != obj.period:
            obj.access_to = None
        super().save_model(request, obj, form, change)
