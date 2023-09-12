FROM python:3.9-alpine3.16

COPY requirements.txt /requirements.txt
COPY . /Store
WORKDIR /Store
EXPOSE 8000
RUN apk add postgresql-client build-base postgresql-dev


RUN pip install -r /requirements.txt

