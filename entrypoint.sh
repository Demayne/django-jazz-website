#!/bin/bash

# Add the project directory to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/app"

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Run the Django development server
python manage.py runserver 0.0.0.0:8000
