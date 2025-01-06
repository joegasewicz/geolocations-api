import pytest
from sqlalchemy.orm import sessionmaker

from app.models import (
    Location as LocationModel,
)
from app.utils.database import get_engine, Model
from app.config import TestConfig


def get_test_engine():
   return get_engine(config=TestConfig())


def get_test_session(engine):
    return sessionmaker(engine)()

# @pytest.fixture(scope="function")
def seed_test_db():
    engine = get_test_engine()
    Model.metadata.drop_all(engine)
    Model.metadata.create_all(engine)
    session = get_test_session(engine)

    location1 = LocationModel(
        town="Barnsley",
        latitude=53.56625,
        longitude=-1.45225,
        iso_3166_1="GB-ENG",
        country="England",
    )
    location2 = LocationModel(
        town="Oxford",
        latitude=51.74196,
        longitude=-1.21169,
        iso_3166_1="GB-ENG",
        country="England",
    )
    session.add(location1)
    session.add(location2)
    session.commit()
