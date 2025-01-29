import os


class Config:
    # Postgres
    PGPORT = os.getenv("PGPORT", 5433)
    PGDATABASE = os.getenv("PGDATABASE", "location_etl_db")
    PGUSER = os.getenv("PGUSER", "admin")
    PGPASSWORD = os.getenv("PGPASSWORD", "admin")
    PGHOST = os.getenv("PGHOST", "0.0.0.0")
    # Server
    VERSION = "v0.1"
    SERVER_PORT = os.getenv("SERVER_PORT", 8888)
    SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")
    # Location Data
    LOCATION_DATA_FILE = "data/Australia_Entire_Dataset.csv"
    SQLALCHEMY_LOGGING = False

class TestConfig(Config):
    # Postgres
    PGPORT = 5434
    PGDATABASE = "location_etl_test_db"
    PGUSER = "admin"
    PGPASSWORD = "admin"
    PGHOST = "localhost"
    # Server
    SERVER_PORT = 8889
