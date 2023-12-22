#!/bin/sh
#  Создание миграций
python3 manage.pu makemigration --no-input
# Мигрирование 
python3 manage.py migrate --no-input
# Сбор статики
python3 manage.py collectstatic --no-input

# Запуск гуникорна на 8000 порту
gunicorn --bind 0.0.0.0:8000 mysite.wsgi 
