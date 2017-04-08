#!/bin/bash


# Make sure data is only loaded on first start
if [ ! -d /data ]; then

  echo "Downloading data..."
  mkdir /data

  echo "Making migrations..."
  # prep migrations
  python manage.py makemigrations >> /dev/null
  echo "Migrating database if necessary"
  python manage.py migrate >> /dev/null


 # Removed in favor of manually populating the database once
 # echo "Loading data..."
 # python manage.py shell --command="import housing_backend.loader"

fi


./manage.py collectstatic --noinput

gunicorn backend.wsgi:application -b :8000
