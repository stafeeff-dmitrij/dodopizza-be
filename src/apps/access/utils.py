import datetime
import logging

from dateutil.relativedelta import relativedelta  # type: ignore
from django.utils import timezone

from apps.access.constants import AccessPeriodChoice

logger = logging.getLogger(__name__)


def get_access_to(access_period: AccessPeriodChoice) -> datetime.datetime:
    """
    Возврат временного периода в формате datetime исходя из переданной константы
    """
    access_to = timezone.now()

    if access_period == AccessPeriodChoice.TEN_MIN:
        access_to += datetime.timedelta(minutes=10)

    elif access_period == AccessPeriodChoice.THIRTY_MIN:
        access_to += datetime.timedelta(minutes=30)

    elif access_period == AccessPeriodChoice.ONE_HOUR:
        access_to += datetime.timedelta(hours=1)

    elif access_period == AccessPeriodChoice.TWO_HOUR:
        access_to += datetime.timedelta(hours=2)

    elif access_period == AccessPeriodChoice.SIX_HOUR:
        access_to += datetime.timedelta(hours=6)

    elif access_period == AccessPeriodChoice.TWELVE_HOUR:
        access_to += datetime.timedelta(hours=12)

    elif access_period == AccessPeriodChoice.ONE_DAY:
        access_to += datetime.timedelta(days=1)

    elif access_period == AccessPeriodChoice.ONE_WEEK:
        access_to += datetime.timedelta(weeks=1)

    elif access_period == AccessPeriodChoice.ONE_MONTH:
        access_to += relativedelta(months=1)

    elif access_period == AccessPeriodChoice.ALWAYS:
        access_to = datetime.datetime.max

    else:
        logger.error('Передано некорректное значение для access_period')

    return access_to
