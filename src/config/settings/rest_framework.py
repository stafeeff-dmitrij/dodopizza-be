REST_FRAMEWORK = {
    # Аутентификация
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'apps.catalog.pagination.CatalogPagination',
    'PAGE_SIZE': 10,
}