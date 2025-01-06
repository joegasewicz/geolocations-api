from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.config import Config, TestConfig


class Model(DeclarativeBase):
    pass


def get_engine(*, config: Config):
    url = URL.create(
        drivername="postgresql",
        username=config.PGUSER,
        password=config.PGPASSWORD,
        host=config.PGHOST,
        database=config.PGDATABASE,
        port=config.PGPORT,
    )
    return create_engine(url, echo=True)


def get_session():
    engine = get_engine(config=Config())
    return sessionmaker(engine)()
