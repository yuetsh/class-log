#!/bin/sh

python manage.py createcachetable
python manage.py collectstatic --noinput
python manage.py migrate --noinput
exec gunicorn --bind 0.0.0.0:8000 classlog.asgi:application -k uvicorn.workers.UvicornWorker