import tornado

from app.handlers import BaseHandler


class HealthHandler(BaseHandler):

    def get(self) -> None:
        data = {
            "endpoint": "/health",
            "status": "OK",
        }
        self.set_header("Content-Type", "application/json")
        self.write(data)
        self.set_status(status_code=200)
