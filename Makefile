DB_NAME=towns_db
DB_USERNAME=admin
DB_PASSWORD=admin
MONGO_VOLUME=mongodb_data
API_PORT=7000
DOCKER_TAG=bandnoticeboard/geolocations-api
DOCKER_NAME=bandnoticeboard_geolocations-api

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
	mongoimport -d bn_database -c towns --file ./towns.json --authenticationDatabase admin --username $(DB_USERNAME) --password $(DB_PASSWORD) --host localhost --port 27017

docker-build:
	docker build --tag $(DOCKER_TAG):latest .

docker-run:
	docker run -p 7000:7000 $(DOCKER_TAG):latest

# private tasks
docker-update:
	docker login
	docker push $(DOCKER_TAG):latest
