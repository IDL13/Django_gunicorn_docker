#!/bin/sh

# cd ..
# cd ./venv/bin/
# . activate.sh --no-input
# cd /app

# pip install django --no-input
# pip install python_dotenv --no-input
# pip insatll psycopg2 --no-input
# pip insatll qrcode --no-input
# pip install bs4 --no-input

python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input

# gunicorn mysite.wsgi:application --bind 0.0.0.0:8085
python3 manage.py runserver 0.0.0.0:8000