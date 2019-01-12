FROM python:3.6.8-alpine3.6

LABEL maintainer="Lucio Delelis <ldelelis@est.frba.utn.edu.ar>"

ADD . /meli_auth
WORKDIR /meli_auth

RUN pip install -r requirements.txt

EXPOSE 8000

ENV MELI_AUTH_CLIENT_ID
ENV MELI_AUTH_CLIENT_SECRET
ENV MELI_AUTH_ROOT_URL "/api/v1"
ENV MELI_AUTH_CALLBACK_URL "http://localhost:8000/api/v1/callback"
ENV MELI_AUTH_MONGO_HOST db
ENV MELI_AUTH_MONGO_PORT 27017
ENV MELI_AUTH_MONGO_DB meli_auth
ENV MELI_AUTH_MONGO_COLLECTION clients


ENTRYPOINT [ "gunicorn", "-c", "gunicorn.py", "meli_auth:app" ]
