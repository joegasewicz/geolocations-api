FROM python:3.10-slim-buster

WORKDIR /geolocations-api

ARG API_DB_NAME
ARG API_DB_USERNAME
ARG API_DB_PASSWORD
ARG API_DB_HOST
ARG API_DB_PORT
ARG SERVER_PORT
ARG SERVER_HOST

ENV API_DB_NAME=${API_DB_NAME}
ENV API_DB_USERNAME=${API_DB_USERNAME}
ENV API_DB_PASSWORD=${API_DB_PASSWORD}
ENV API_DB_HOST=${API_DB_HOST}
ENV API_DB_PORT=${API_DB_PORT}
ENV SERVER_PORT=${SERVER_PORT}
ENV SERVER_HOST=${SERVER_HOST}

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY api api

RUN pipenv install --deploy

CMD [ "pipenv","run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "6000"]
