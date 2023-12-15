#!/bin/sh
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

# gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
gunicorn --bind 0.0.0.0:8000 mysite.wsgi 
# python3 manage.py runserver 0.0.0.0:443