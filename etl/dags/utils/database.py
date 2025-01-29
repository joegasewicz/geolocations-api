from .config import Config


def get_pg_conn(config: Config) -> str:
    return (f"postgresql+psycopg2://"
            f"{config.DB_USERNAME}:"
            f"{config.DB_PASSWORD}@"
            f"{config.DB_HOST}:"
            f"{config.DB_PORT}/"
            f"{config.DB_NAME}")
