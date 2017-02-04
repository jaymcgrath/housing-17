#!/bin/bash

echo "Migrating database..."
while ! ./manage.py migrate >> /dev/null 2>&1 ; do
  sleep 1
done

echo "Loading data..."
./manage.py shell --command="import housing_backend.loader"

./manage.py collectstatic --noinput

gunicorn backend.wsgi:application -b :8000
