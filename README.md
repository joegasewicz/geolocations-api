# geolocations-api
United Kingdom Town / City geolocations with FastAPI  &amp; Mongo

# Build container
To build a custom image or extend the api run the following cmds
```bash
# update the following variables as required
API_PORT=7000
API_HOST=locahost
# API variables
API_DB_NAME=towns_db
API_DB_USERNAME=admin
API_DB_PASSWORD=admin
API_DB_HOST=host.docker.internal
API_DB_PORT=27017

# Then build & run
make docker-build
make docker-run
```

# Build locally instructions
Open `Makefile` in your ide & update the following varables as required:
```bash
DB_NAME=<YOUR_DB_NAME>
DB_USERNAME=<YOUR_DB_USERNAME>
DB_PASSWORD=<YOUR_DB_PASSWORD>
```

Make sure you have `mongoimport` command available & run the below command to import the towns JSON dump
```bash
make mongo-import-towns
```
