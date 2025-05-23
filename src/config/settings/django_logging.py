LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'color': {
            '()': 'colorlog.ColoredFormatter',
            'format': '%(log_color)s%(asctime)-8s %(levelname)s - %(name)s.py | '
                      'func:%(funcName)s (%(lineno)s) - %(message)s',
            'log_colors': {
                'DEBUG': 'white',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'bold_red',
            },
        },
    },
    'handlers': {
        'console': {'class': 'logging.StreamHandler', 'formatter': 'color'},
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
