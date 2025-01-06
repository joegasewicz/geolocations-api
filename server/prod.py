import asyncio
import tornado
import os
from typing import List

# We want a KeyError if any of these variables are not defined
# API_DB_NAME = os.environ["API_DB_NAME"]
# API_DB_USERNAME = os.environ["API_DB_USERNAME"]
# API_DB_PASSWORD = os.environ["API_DB_PASSWORD"]
# API_DB_HOST = os.environ["API_DB_HOST"]
# API_DB_PORT = os.environ["API_DB_PORT"]


from app import make_app
from app.utils.logger import logger
from app.config import Config


async def main(config: Config):
    app = make_app(config)
    app.listen(config.SERVER_PORT)
    await asyncio.Event().wait()

if __name__ == "__main__":
    config = Config()
    logger.info(f"Starting server on http://127.0.0.1:{config.SERVER_PORT}")
    asyncio.run(main(config))
