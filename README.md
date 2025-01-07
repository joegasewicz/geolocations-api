[![Makefile CI](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml/badge.svg)](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml)
# Geolocations Api
REST API & Apache Airflow project that returns location data.

### Version 2
The latest version for geolocations-api is available here:
```
docker pull bandnoticeboard/geolocations-api:latest
```

### ETL
ETL pipelines with [Apache Airflow](https://airflow.apache.org/). See [etl](etl)

#### Run Apache Airflow
`cd etl && make airflow`

### Server
A tornado REST api. See [server](server)

## Quick Start
1. Run docker compose `make docker-compose-local`
2. Clone & cd into the root folder of this repo
3. Run Airflow to provision the Postgres database with the geolocation data.
```bash
# This will create a `locations` table in your db from the `TODO` dump
TODO
# OR run the following cmd:
TODO
```
4. Run the latest version of geolocations-api
```bash
docker run bandnoticeboard/geolocations-api
```
# Example Queries
Currently, the api returns 5 entrees per query

Use the `name` query param to fetch the first 5 similar results:
```bash
curl http://localhost:8000/towns?name=col
```
Will return 
```bash
{
    "endpoint": "/locations",
    "locations": [
        {
            "town": "Gloucester",
            "latitude": 51.84688,
            "longitude": -2.22568,
            "iso_3166_1": "GB-ENG",
            "country": "England"
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
      - "8000:8000"
    environment:
      API_DB_NAME: towns_db
      API_DB_USERNAME: admin
      API_DB_PASSWORD: admin
      API_DB_HOST: host.docker.internal
      API_DB_PORT: 5433
```
## Contributing
PR's are welcome for bug fixes or open an issue.

For new features or adding new country geolocation dumps please open an issue first.