#!/bin/bash

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Make migrations
echo "Making migrations..."
python manage.py makemigrations
python manage.py migrate

exec "$@"