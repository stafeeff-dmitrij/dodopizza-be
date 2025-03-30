import datetime

from dateutil.relativedelta import relativedelta  # type: ignore
from django.test import TestCase, tag
from django.utils import timezone

from apps.access.constants import AccessPeriodChoice
from apps.access.utils import get_access_to


class TestUtils(TestCase):
    """
    Тестирование утилит
    """

    @classmethod
    def setUp(self):
        self.access_to = timezone.now()

    @tag('utils')
    def test_get_access_to_ten_min(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 10 минут
        """
        control_res = self.access_to + datetime.timedelta(minutes=10)
        access_to = get_access_to(access_period=AccessPeriodChoice.TEN_MIN)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_thirty_min(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 30 минут
        """
        control_res = self.access_to + datetime.timedelta(minutes=30)
        access_to = get_access_to(access_period=AccessPeriodChoice.THIRTY_MIN)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_one_hour(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 1 час
        """
        control_res = self.access_to + datetime.timedelta(hours=1)
        access_to = get_access_to(access_period=AccessPeriodChoice.ONE_HOUR)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_two_hour(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 2 часа
        """
        control_res = self.access_to + datetime.timedelta(hours=2)
        access_to = get_access_to(access_period=AccessPeriodChoice.TWO_HOUR)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_six_hour(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 6 часов
        """
        control_res = self.access_to + datetime.timedelta(hours=6)
        access_to = get_access_to(access_period=AccessPeriodChoice.SIX_HOUR)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_twelve_hour(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 12 часов
        """
        control_res = self.access_to + datetime.timedelta(hours=12)
        access_to = get_access_to(access_period=AccessPeriodChoice.TWELVE_HOUR)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_one_day(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 1 день
        """
        control_res = self.access_to + datetime.timedelta(days=1)
        access_to = get_access_to(access_period=AccessPeriodChoice.ONE_DAY)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_one_week(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 1 неделю
        """
        control_res = self.access_to + datetime.timedelta(weeks=1)
        access_to = get_access_to(access_period=AccessPeriodChoice.ONE_WEEK)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_one_month(self):
        """
        Проверка корректности возврата времени при передаче продолжительности в 1 месяц
        """
        control_res = self.access_to + relativedelta(months=1)
        access_to = get_access_to(access_period=AccessPeriodChoice.ONE_MONTH)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_always(self):
        """
        Проверка корректности возврата времени при передаче продолжительности навсегда
        """
        control_res = datetime.datetime.max
        access_to = get_access_to(access_period=AccessPeriodChoice.ALWAYS)

        self.assertEqual(control_res.replace(microsecond=0), access_to.replace(microsecond=0))

    @tag('utils')
    def test_get_access_to_incorrect(self):
        """
        Проверка корректности возврата времени при передаче некорректной продолжительности
        """
        access_to = get_access_to(access_period='20m')

        self.assertEqual(self.access_to.replace(microsecond=0), access_to.replace(microsecond=0))
