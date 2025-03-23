from django.test import tag
from faker import Faker

from apps.access.serializers import AccessRequestSerializer
from apps.access.tests.base import TestBase

fake = Faker()


class TestAccessRequestSerializer(TestBase):
    """
    Тестирование сериализатора для проверки входных данных при запросе доступа к сайту
    """

    @classmethod
    def setUpTestData(cls):
        """
        Клиент с недопущенным ip адресом
        """
        super().setUpTestData()
        cls.invalid_email = 'testmail.com'
        cls.invalid_comment = fake.text(max_nb_chars=500)

    @tag('serializers')
    def test_valid_data(self):
        """
        Проверка валидных данных
        """
        serializer = AccessRequestSerializer(data=self.access_data)
        self.assertTrue(serializer.is_valid())

    @tag('serializers')
    def test_comment_max_length(self):
        """
        Проверка невалидного комментария по кол-ву символов
        """
        self.access_data['comment'] = self.invalid_comment
        serializer = AccessRequestSerializer(data=self.access_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('comment', serializer.errors)
        self.assertEqual(serializer.errors['comment'][0].code, 'max_length')

    @tag('serializers')
    def test_invalid_email(self):
        """
        Проверка невалидного email
        """
        self.access_data['email'] = self.invalid_email
        serializer = AccessRequestSerializer(data=self.access_data)

        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)
        self.assertEqual(serializer.errors['email'][0].code, 'invalid')
