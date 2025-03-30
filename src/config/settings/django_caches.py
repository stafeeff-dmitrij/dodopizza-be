from config.settings import CACHE_TIMEOUT, REDIS_DB, REDIS_HOST, REDIS_PORT

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'MAX_ENTRIES': 1000
        },
        'TIMEOUT': CACHE_TIMEOUT
    }
}
