#!/bin/bash

set -e

python manage.py check_db --settings=core.settings
python manage.py makemigrations --settings=core.settings
python manage.py migrate --settings=core.settings
python manage.py collectstatic --no-input --settings=core.settings
python manage.py create_user --settings=core.settings

echo "========================================="
echo "RIZAL, YOUR PROJECT IS UP AND RUNNING NOW"
echo "========================================="

export DJANGO_SETTINGS_MODULE=core.settings

gunicorn --bind 0.0.0.0:8000 core.wsgi:application