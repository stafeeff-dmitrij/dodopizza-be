from rest_framework import serializers

from apps.access.models import AccessByIP


class AccessRequestSerializer(serializers.ModelSerializer):
    """
    Схема для проверки данных при создании запроса на доступ к сайту
    """

    comment = serializers.CharField(max_length=250)

    class Meta:
        model = AccessByIP
        fields = ('email', 'comment')
