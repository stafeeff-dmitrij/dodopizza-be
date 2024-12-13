import os
from pathlib import Path

import environ


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_DIR = BASE_DIR.parent

env = environ.Env(DEBUG=(bool, False), PORT=(str, ''), HOST=(str, 'localhost'))
environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))

PROJECT_TITLE = 'ДОДО ПИЦЦА'
PROJECT_DESCRIPTION = 'Самая вкусная пицца на свете'
PROJECT_VERSION = '0.0.1'

SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DJANGO_DEBUG')
ALLOWED_HOSTS = []
WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'


DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')