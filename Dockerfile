FROM python:3.5
ENV PYTHONUNBUFFERED 1
ADD ./requirements.txt /provision/
ADD https://raw.githubusercontent.com/hackoregon/housing-17/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv /provision/
# ADD ./backend/ /code/
WORKDIR /provision/
RUN pip install -r requirements.txt
WORKDIR /code/
# RUN ./manage.py migrate
# RUN ./manage.py shell --command="import housing_backend.loader"
