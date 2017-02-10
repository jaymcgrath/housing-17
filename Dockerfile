FROM python:3.5
ENV PYTHONUNBUFFERED 1
ADD ./requirements.txt /provision/
WORKDIR /provision/
RUN pip install -r requirements.txt
WORKDIR /code/
