[![Makefile CI](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml/badge.svg)](https://github.com/joegasewicz/geolocations-api/actions/workflows/makefile.yml)
# Geolocations Api
REST api & Apache Airflow project that returns location data.

### Version 2
Work in progress 🚧, please call back soon...

### ETL
ETL pipelines with [Apache Airflow](https://airflow.apache.org/). See [etl](etl)

#### Run Apache Airflow
`cd etl && make airflow`

### Server
A tornado REST api. See [server](server)

### Endpoints
`/api/v0.1/locations`:

```
{
    "endpoint": "/locations",
    "locations": [
        {
            "town": "Barnsley",
            "latitude": 53.56625,
            "longitude": -1.45225,
            "iso_3166_1": "GB-ENG",
            "country": "England"
        },
        ...
}        
```

## Contributing
PR's are welcome for bug fixes or open an issue.

For new features or adding new country geolocation dumps please open an issue first.
