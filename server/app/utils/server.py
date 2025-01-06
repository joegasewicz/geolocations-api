from app.config import Config


def get_version(config: Config):
    return f"/api/{config.VERSION}"
