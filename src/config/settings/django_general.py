import os
import tomllib
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent  # src
ROOT_DIR = BASE_DIR.parent

env = environ.Env()
environ.Env.read_env(os.path.join(ROOT_DIR, '.env'))

# Конфиги проекта
pyproject_file = os.path.join(ROOT_DIR, 'pyproject.toml')

with open(pyproject_file, 'rb') as f:
    pyproject_data = tomllib.load(f)

PROJECT_TITLE = pyproject_data['project']['name']
PROJECT_DESCRIPTION = pyproject_data['project']['description']
PROJECT_VERSION = pyproject_data['project']['version']

# Django
SECRET_KEY = env('DJANGO_SECRET_KEY')
DEBUG = env('DEBUG', cast=bool, default=False)
HTTP_PROTOCOL = env('HTTP_PROTOCOL', default='http')
HOST = env('HOST', default='localhost')
PORT = env('PORT', cast=int, default=8000)

ALLOWED_HOSTS: list[str] = ['*']
CORS_ALLOWED_ORIGINS = env('ALLOWED_ORIGINS').split(',')

WSGI_APPLICATION = 'config.wsgi.application'
ROOT_URLCONF = 'config.urls'

# DB
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
DB_NAME = env('DB_NAME')
DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')

# Redis
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
REDIS_DB = env('REDIS_DB')

# Кэширование
CACHE_TIMEOUT = env('CACHE_TIMEOUT', cast=int, default=3600)