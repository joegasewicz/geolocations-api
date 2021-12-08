FROM python:3.10-slim-buster

WORKDIR /geolocations-api

RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
COPY api api

RUN pipenv install --deploy

CMD [ "pipenv","run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "7000"]
