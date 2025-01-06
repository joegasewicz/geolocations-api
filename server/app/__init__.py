import tornado

from app.handlers import (
    HealthHandler,
    LocationHandler,
)
from app.config import Config
from app.utils.server import get_version


def make_app(config: Config) -> tornado.web.Application:
    version = get_version(config)
    return tornado.web.Application([
        (fr"{version}/health", HealthHandler),
        (fr"{version}/locations", LocationHandler),
    ])
