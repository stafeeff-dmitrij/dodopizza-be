#!/bin/sh
cd src || exit
python manage.py test
