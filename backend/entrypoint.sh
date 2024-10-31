#!/bin/bash

set -e

if [ "$ENVIRONMENT" = "production" ]; then
    echo "Collecting static files"
    python manage.py collectstatic --clear --noinput
    echo "Running migrations"
    python manage.py migrate
    echo "Running in production mode"
    exec gunicorn -c gunicorn_conf.py
elif [ "$ENVIRONMENT" = "development" ]; then
    echo "Running in development mode"
    exec python manage.py runserver 0.0.0.0:8000
else
    echo "ENVIRONMENT variable is not set"
fi
