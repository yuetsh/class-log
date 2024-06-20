#!/bin/sh

python manage.py migrate
exec gunicorn --bind 0.0.0.0:8000 classlog.asgi:application -k uvicorn.workers.UvicornWorker