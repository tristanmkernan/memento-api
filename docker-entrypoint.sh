#!/bin/sh

# https://stackoverflow.com/a/33993532
# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Start server
echo "Starting server"
uwsgi /code/uwsgi.ini
