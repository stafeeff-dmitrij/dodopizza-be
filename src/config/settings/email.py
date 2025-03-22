from config.settings import env

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Отправка email
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Вывод email в консоль

EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER
