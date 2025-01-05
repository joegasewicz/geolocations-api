from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase

from app.config import Config


class Model(DeclarativeBase):
    pass


def get_engine(*, config: Config):
    url = URL.create(
        drivername="postgresql",
        username="admin",
        password="admin",
        host="localhost",
        database="locations_db",
    )
    return create_engine(url, echo=True)


engine = get_engine(config=Config())
