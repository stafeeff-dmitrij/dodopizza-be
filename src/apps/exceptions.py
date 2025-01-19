from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidDataResponseException(APIException):
    """
    Исключение для возврата ответа при передаче невалидных данных
    """

    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Переданы невалидные данные'
