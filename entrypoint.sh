#!/bin/sh

python manage.py collectstatic --on-input
python manage.py migrate --on-input
exec gunicorn --bind 0.0.0.0:8000 classlog.asgi:application -k uvicorn.workers.UvicornWorker