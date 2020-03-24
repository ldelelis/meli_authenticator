FROM python:3.7-alpine

LABEL maintainer="Lucio Delelis <me@ldelelis.dev>"

COPY requirements.txt /

RUN pip install -r requirements.txt

ADD . /usr/src/app
WORKDIR /usr/src/app

