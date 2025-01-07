import asyncio

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
