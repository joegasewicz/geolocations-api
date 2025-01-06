from unittest import mock
from unittest.mock import patch, MagicMock
from tornado.testing import AsyncHTTPTestCase, gen_test
from tornado.web import Application

from app import make_app
from app.config import TestConfig
from tests.fixtures.database import seed_test_db, get_test_engine, get_test_session


class LocationHandlerTest(AsyncHTTPTestCase):

    def setup_method(self, method):
        seed_test_db()

    def get_app(self) -> Application:
        return make_app(TestConfig())

    # def test_get_locations(self):
    #     seed_test_db()
    #     response = self.fetch("/api/v0.1/locations")
    #     self.assertEqual(response.code, 200)
    #     self.assertEqual(response.body.decode(), '{"endpoint": "/locations", "locations": []}')

    @patch("app.utils.database.get_session", MagicMock(return_value=get_test_session(get_test_engine())))
    def test_get_locations_params(self):
        response = self.fetch("/api/v0.1/locations?town=b")
        # self.assertEqual(response.code, 200)
        self.assertEqual(response.body.decode(), '{"endpoint": "/locations", "locations": []}')
