command = "/home/root-user/Рабочий стол/programs/python/env/bin/gunicorn"
pythonpath = "/home/root-user/Рабочий стол/programs/python/Django_gunicorn_docker/mysite/mysite"
bind = "127.0.0.1:8001"
workers = 5
user = "root-user"
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = "DJANGO_SETTINGS_MODULE=mysite.mysite.settings"