#!/bin/sh
cd src || exit
python manage.py migrate
python manage.py load_initial_data
python manage.py collectstatic --noinput
gunicorn config.wsgi:application --workers 4 --bind=0.0.0.0:8000 --access-logfile - --error-logfile -
