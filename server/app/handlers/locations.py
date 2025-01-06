import tornado
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from app.models import (
    Location as LocationModel,
)
from app.schemas import (
    Location as LocationSchema,
)
from app.utils.database import get_session
from app.utils.logger import logger


class LocationHandler(tornado.web.RequestHandler):

    def get(self) -> None:
        self.set_header("Content-Type", "application/json")
        town_query = self.get_query_argument("town", default=None)
        if town_query is None:
            data = {
                "endpoint": "/locations",
                "locations": [],
            }
            self.write(data)
            self.set_status(status_code=200)
            return
        location_list = []
        try:
            session = get_session()
            q = select(LocationModel).where(LocationModel.town.ilike(f"%{town_query}%"))
            q = q.limit(5)
            locations = session.execute(q).all()
            for location in locations:
                location_list.append(LocationSchema().dump(location[0]))
            data = {
                "endpoint": "/locations",
                "locations": location_list,
            }

            self.write(data)
            self.set_status(status_code=200)
        except Exception as err:
            logger.error("Error!", exc_info=err)
            print(str(err))
            self.set_status(400)
            self.write({
                "error": "Error fetching data",
            })


