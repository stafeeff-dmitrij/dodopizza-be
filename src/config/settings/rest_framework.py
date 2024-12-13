REST_FRAMEWORK = {
    # Аутентификация
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],

    # drf-spectacular
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    # парсеры для обработки входящих данных
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser'  # только JSON
    ],
}
