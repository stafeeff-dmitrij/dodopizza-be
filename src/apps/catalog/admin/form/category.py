from django import forms
from django.core.exceptions import ValidationError

from apps.catalog.models import Category
from apps.catalog.utils import check_max_level_category


class SubcategoryModelForm(forms.ModelForm):
    """
    Форма создания и редактирования подкатегории
    """

    class Meta:
        model = Category
        fields = ('order', 'name', 'status')

    def clean(self):
        """
        Проверка уровня вложенности и статуса подкатегории
        """
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent')
        name = cleaned_data.get('name')
        status = cleaned_data.get('status')

        if status is True and parent.status is False:
            raise ValidationError(
                f'Нельзя активировать подкатегорию "{name}", если ее родительская категория "{parent.name}" отключена!'
            )

        if not check_max_level_category(category=parent, parent=True):
            raise ValidationError('Превышена максимальная вложенность категорий в 2уровня! Текущая вложенность: 3')

        return cleaned_data
