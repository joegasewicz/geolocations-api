import os


class Config:
    # Postgres
    PGPORT = os.getenv("PGPORT", 5433)
    PGDATABASE = os.getenv("PGDATABASE", "locations_db")
    PGUSER = os.getenv("PGUSER", "admin")
    PGPASSWORD = os.getenv("PGPASSWORD", "admin")
    PGHOST = os.getenv("PGHOST", "localhost")
    # Server
    VERSION = "v0.1"
    SERVER_PORT = os.getenv("SERVER_PORT", 8888)


class TestConfig(Config):
    # Postgres
    PGPORT = 5434
    PGDATABASE = "location_etl_test_db"
    PGUSER = "admin"
    PGPASSWORD = "admin"
    PGHOST = "localhost"
    # Server
    SERVER_PORT = 8889
