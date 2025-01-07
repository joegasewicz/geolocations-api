[![Makefile CI](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml/badge.svg)](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml)
# Geolocations Api
REST API & Apache Airflow project that returns location data.

### Version 2
The latest version for geolocations-api is available here:
```
docker pull bandnoticeboard/geolocations-api:2.1.0-alpha
```
### ETL
ETL pipelines with [Apache Airflow](https://airflow.apache.org/). See [etl](etl)

#### Run Apache Airflow
`cd etl && make airflow`

### Server
A tornado REST api. See [server](server)

## Quick Start
1. Run docker compose `docker run bandnoticeboard/geolocations-api:2.1.0-alpha`

# Example Queries
Currently, the api returns 5 entrees per query

Use the `town` query param to fetch the first 5 similar results:
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
services:

  geolocations_api:
    image: "bandnoticeboard/geolocations-api:latest"
    ports:
      - "8000:8000"
    environment:
      PGPORT: 5433
      PGDATABASE: location_etl_db
      PGUSER: admin
      PGPASSWORD: admin
      PGHOST: host.docker.internal
      SERVER_PORT: 8000
      SERVER_HOST: 0.0.0.0
```
## Contributing
PR's are welcome for bug fixes or open an issue.

For new features or adding new country geolocation dumps please open an issue first.