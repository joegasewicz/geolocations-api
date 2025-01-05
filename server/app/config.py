import os


class Config:
    SERVER_PORT = os.getenv("SERVER_PORT", 8888)
    PGPORT = os.getenv("PGPORT", 5434)
    PGDATABASE = os.getenv("PGDATABASE", "locations_db")
    PGUSER = os.getenv("PGUSER", "admin")
    PGPASSWORD = os.getenv("PGPASSWORD", "admin")
