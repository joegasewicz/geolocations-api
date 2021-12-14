[![Makefile CI](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml/badge.svg)](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml)
# Geolocations Api
Geolocations with FastAPI  &amp; Mongo. United Kingdom is currently the only region supported but other regions will be supported in the future.

## Quick Start
1. Run mongodb
2. Clone & cd into the root folder of this repo
3. Setup a mongo database as a container - see [docker-compose example](https://github.com/joegasewicz/geolocations-api/blob/master/docker-compose.example.yml)
4. Make sure you have `mongoimport` cmd installed & run the following make task:
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

## Docker Compose Example
See [docker-compose.example.yml](https://github.com/joegasewicz/geolocations-api/docker-compose.example.yml)
```bash
version: "3"

services:

  geolocations_api:
    image: "bandnoticeboard/geolocations-api:latest"
    ports:
      - "7000:7000"
    environment:
      API_DB_NAME: towns_db
      API_DB_USERNAME: admin
      API_DB_PASSWORD: admin
      API_DB_HOST: host.docker.internal
      API_DB_PORT: 27017
```
## Contributing
PR's are welcome for bug fixes or open an issue.

For new features or adding new country geolocation dumps please open an issue first.
