import tornado
import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
)

from app.handlers import (
    HealthHandler,
    LocationHandler,
)
from app.models import (
    Location as LocationModel,
)
from app.config import Config
from app.utils.server import get_version
from app.utils.database import engine, Session, Model
from app.utils.logger import logger


def make_app(config: Config) -> tornado.web.Application:
    """
    :param config:
    :return:
    """
    # Only create tables that don't already exist
    metadata = MetaData()
    metadata.reflect(bind=engine)
    locations_table = metadata.tables.get("locations")
    if locations_table is None:
        logger.info(f"Loading data from {config.LOCATION_DATA_FILE}")
        df = pd.read_csv(config.LOCATION_DATA_FILE, index_col=0)
        session = Session()
        try:
            Model.metadata.create_all(engine)
            df_dict =df.to_dict("records")
            for record in df_dict:
                location = LocationModel(
                    town=record["town"],
                    latitude=record["latitude"],
                    longitude=record["longitude"],
                    country=record["country"],
                )
                session.add(location)
            session.commit()
            session.close()
        except SQLAlchemyError as err:
            session.rollback()
            logger.error(f"Error dumping {config.LOCATION_DATA_FILE}", exc_info=err)
        finally:
           engine.dispose()
    else:
        logger.info("Skipping dumping locations data")

    version = get_version(config)
    return tornado.web.Application([
        (fr"{version}/health", HealthHandler),
        (fr"{version}/locations", LocationHandler),
    ])
