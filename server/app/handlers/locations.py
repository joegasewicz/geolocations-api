import tornado


class LocationHandler(tornado.web.RequestHandler):

    def get(self) -> None:
        data = {
            "endpoint": "/locations"
        }

        self.set_header("Content-Type", "application/json")
        self.write(data)
        self.set_status(status_code=200)
