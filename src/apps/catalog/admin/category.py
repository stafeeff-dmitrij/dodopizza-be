from django.contrib import admin, messages
from mptt.admin import DraggableMPTTAdmin

from apps.catalog.admin.actions.activate import activate_records
from apps.catalog.admin.actions.deactivate import deactivate_records
from apps.catalog.admin.filter.parent_category import ParentCategoryFilter
from apps.catalog.models import Category
from apps.catalog.utils.status import change_status_child_records
from config.settings import PROJECT_VERSION

admin.site.site_title = 'ДОДО ПИЦЦА'
admin.site.site_header = f"ДОДО ПИЦЦА (v{PROJECT_VERSION}). Административная панель"


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

    # Отключение / включение записей
    actions = (deactivate_records, activate_records)

    def save_model(self, request, obj, form, change):
        """
        Проверка уровня вложенности категории перед сохранением
        """

        # изменение записи
        if change:
            new_status = form.cleaned_data.get('status')

            # запрещаем включать подкатегорию, если родительская категория отключена
            if obj.parent and obj.parent.status is False and new_status is True:
                messages.set_level(request, messages.ERROR)  # Меняем уровень сообщения на ERROR
                messages.add_message(
                    request,
                    level=messages.ERROR,
                    message=f'Нельзя активировать подкатегорию, если ее родительская категория "{obj.parent.name}" отключена!'
                )
                return

            # меняем для дочерних категорий статус как у родителя
            if not obj.parent:
                change_status_child_records(records=[obj], active=new_status)

        # для новых записей максимальная вложенность категорий 2
        if obj.parent:
            max_indent = 2
            lvl = obj.parent.level + 1

            if lvl >= max_indent:
                messages.set_level(request, messages.ERROR)  # Меняем уровень сообщения на ERROR
                messages.add_message(
                    request,
                    level=messages.ERROR,
                    message=f'Превышена максимальная вложенность категорий в {max_indent} уровня! '
                    f'Текущая вложенность: {lvl + 1}',
                )
                return

        super().save_model(request, obj, form, change)
