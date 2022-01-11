# Mongodb variables
DB_NAME=towns_db
DB_USERNAME=admin
DB_PASSWORD=admin
MONGO_VOLUME=mongodb_data
# Docker variables
DOCKER_TAG=bandnoticeboard/geolocations-api
DOCKER_NAME=bandnoticeboard_geolocations-api
# API variables
API_DB_NAME=towns_db
API_DB_USERNAME=admin
API_DB_PASSWORD=admin
API_DB_HOST=host.docker.internal
API_DB_PORT=27017

locations-api-server:
	pipenv run uvicorn api.main:app --reload

docker-create-volumes:
	docker volume create --name=$(MONGO_VOLUME)

docker-rm-volumes:
	docker rm $(MONGO_VOLUME)

docker-compose-up:
	make docker-create-volumes
	docker-compose up

mongo-import-towns:
	mongoimport -d $(DB_NAME) -c towns --file ./towns.json --authenticationDatabase admin --username $(DB_USERNAME) --password $(DB_PASSWORD) --host localhost --port 27017

docker-build:
	docker build \
  --build-arg API_DB_NAME=$(API_DB_NAME) \
  --build-arg API_DB_USERNAME=$(API_DB_USERNAME) \
  --build-arg API_DB_PASSWORD=$(API_DB_PASSWORD) \
  --build-arg API_DB_HOST=$(API_DB_HOST) \
  --build-arg API_DB_PORT=$(API_DB_PORT) \
  --tag $(DOCKER_TAG):latest .

docker-run:
	docker run -p 7000:7000 $(DOCKER_TAG):latest

# private tasks
docker-push:
	docker login --username=$(DOCKER_USERNAME) --password=$(DOCKER_PASSWORD)
	docker push $(DOCKER_TAG):latest
