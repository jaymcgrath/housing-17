#!/bin/bash

echo "Downloading data..."
mkdir /data
wget \
  -O /data/SoHAffordabilityDatabyNeighborhoodUpload.csv \
  https://raw.githubusercontent.com/hackoregon/housing-17/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv

echo "Migrating database..."
while ! ./manage.py migrate >> /dev/null 2>&1 ; do
  sleep 1
done

echo "Loading data..."
./manage.py shell --command="import housing_backend.loader"

./manage.py collectstatic --noinput

gunicorn backend.wsgi:application -b :8000
