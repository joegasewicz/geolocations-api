# Docker variables
DOCKER_TAG=2.1.0
DOCKER_NAME=bandnoticeboard/geolocations-api

# Server Variables
PGPORT=5433
PGDATABASE=location_etl_db
PGUSER=admin
PGPASSWORD=admin
PGHOST=host.docker.internal
SERVER_PORT=8000
SERVER_HOST=0.0.0.0

locations-api-server:
	pipenv run python prod.py

docker-compose-up:
	make docker-create-volumes
	docker-compose up

docker-build:
	docker build \
  --build-arg PGPORT=$(PGPORT) \
  --build-arg PGDATABASE=$(PGDATABASE) \
  --build-arg PGUSER=$(PGUSER) \
  --build-arg PGPASSWORD=$(PGPASSWORD) \
  --build-arg PGHOST=$(PGHOST) \
  --build-arg SERVER_PORT=$(SERVER_PORT) \
  --build-arg SERVER_HOST=$(SERVER_HOST) \
  --tag $(DOCKER_NAME):$(DOCKER_TAG) .

docker-run:
	docker run -p $(SERVER_PORT):$(SERVER_PORT) $(DOCKER_NAME):$(DOCKER_TAG)

docker-push:
	docker push $(DOCKER_NAME):$(DOCKER_TAG)
