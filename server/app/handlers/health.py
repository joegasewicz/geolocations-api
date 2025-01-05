import tornado


class HealthHandler(tornado.web.RequestHandler):

    def get(self) -> None:
        data = {
            "status": "OK",
        }
        self.set_header("Content-Type", "application/json")
        self.write(data)
        self.set_status(status_code=200)
