[![Makefile CI](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml/badge.svg)](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml)
# Geolocations Api
United Kingdom Town / City geolocations with FastAPI  &amp; Mongo

# Quick Start
1. Run mongodb
2. Clone & cd into the root folder of this repo
3. Makre you have `mongoimport` cmd installed & run the following make task:
```bash
# This will create a `towns` table in your db from the `towns.json` dump
make mongo-import-towns
# OR run the following cmd:
mongoimport -d bn_database -c towns --file ./towns.json --authenticationDatabase admin --username <YOUR_USERNAME> --password <YOUR_PASSWORD> --host localhost --port 27017
```
4. Run the latest version of geolocations-api
```bash
docker run bandnoticeboard/geolocations-api
```
# Example Queries
Currently, the api returns 5 entrees per query

Use the `name` query param to fetch the first 5 similar results:
```bash
curl http://localhost:7000/towns?name=col
```
Will return 
```bash
[
    {
        longitude: -6.32584,
        latitude: 58.2798,
        type: "Other",
        country: "Scotland",
        county: "Na h-Eileanan an Iar",
        reference: "COL",
        town: "Col",
        id: "56c4b2f97c82251d12547b6b"
    },
    ... # plus 4 other entrees
]
```

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
