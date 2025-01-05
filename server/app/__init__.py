import tornado

from app.handlers import (
    HealthHandler,
    LocationHandler,
)
from app.config import Config


def make_app(config: Config) -> tornado.web.Application:
    return tornado.web.Application([
        (r"/health", HealthHandler),
        (r"/locations", LocationHandler),
    ])
