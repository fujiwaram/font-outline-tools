FROM python:3.7-alpine3.9

RUN pip install fonttools

WORKDIR /app
ADD . /app