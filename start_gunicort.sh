#!/bin/bash

cd ..
cd env/bin
source activate
cd ..
cd ..
cd Django_gunicorn_docker 
cd mysite
gunicorn --bind 127.0.0.1:8001 mysite.wsgi