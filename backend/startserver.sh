#!/bin/bash

./manage.py collectstatic --noinput
gunicorn backend.wsgi:application -b :8000
