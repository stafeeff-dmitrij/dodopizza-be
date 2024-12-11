from config.settings.django_general import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASS


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DATABASES = {
    'default': {
        "ENGINE": 'django.db.backends.postgresql',
        "HOST": DB_HOST,
        'PORT': DB_PORT,
        "NAME": DB_NAME,
        "USER": DB_USER,
        "PASSWORD": DB_PASS,
    },
}