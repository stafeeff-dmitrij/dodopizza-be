from django.contrib import admin, messages
from mptt.admin import DraggableMPTTAdmin

from apps.catalog.admin.actions import activate_record, deactivate_records
from apps.catalog.admin.filter import ParentCategoryFilter
from apps.catalog.admin.form import SubcategoryModelForm
from apps.catalog.models import Category
from apps.catalog.utils import change_status_child_records, check_max_level_category
from config.settings import PROJECT_VERSION

admin.site.site_title = 'ДОДО ПИЦЦА'
admin.site.site_header = f"ДОДО ПИЦЦА (v{PROJECT_VERSION}). Административная панель"


class SubcategoryInline(admin.StackedInline):
    """
    Подкатегории
    """

    model = Category
    extra = 0
    ordering = ('order',)
    verbose_name = 'Подкатегория'
    verbose_name_plural = 'Подкатегории'

    form = SubcategoryModelForm


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    """
    Категории товаров
    """

    list_display = ('id', 'order', 'name', 'parent', 'status')
    list_display_links = ('id', 'name')
    list_filter = ('status', ParentCategoryFilter)
    search_fields = ('name',)
    list_editable = ('status',)
    ordering = ('order',)

    inlines = [SubcategoryInline]

    actions = (deactivate_records, activate_record)  # Отключение / включение записей

    def save_model(self, request, obj, form, change):
        """
        Проверка статусов и уровня вложенности категорий перед сохранением
        """

        # изменение записи
        if change:
            new_status = form.cleaned_data.get('status')

            if obj.parent and obj.parent.status is False and new_status is True:
                messages.set_level(request, messages.ERROR)  # Меняем уровень сообщения на ERROR
                messages.add_message(
                    request,
                    level=messages.ERROR,
                    message=f'Нельзя активировать подкатегорию "{obj.name}", '
                    f'если ее родительская категория "{obj.parent.name}" отключена!'
                )
                return

            # при отключении категории также отключаем все подкатегории
            if not obj.parent and new_status is False:
                change_status_child_records(records=[obj], active=new_status)

        if obj.parent and not check_max_level_category(category=obj):
            messages.set_level(request, messages.ERROR)  # Меняем уровень сообщения на ERROR
            messages.add_message(
                request,
                level=messages.ERROR,
                message='Превышена максимальная вложенность категорий в 2 уровня! Текущая вложенность: 3'
            )
            return

        super().save_model(request, obj, form, change)
