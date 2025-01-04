import os
from typing import List



# We want a KeyError if any of these variables are not defined
API_DB_NAME = os.environ["API_DB_NAME"]
API_DB_USERNAME = os.environ["API_DB_USERNAME"]
API_DB_PASSWORD = os.environ["API_DB_PASSWORD"]
API_DB_HOST = os.environ["API_DB_HOST"]
API_DB_PORT = os.environ["API_DB_PORT"]
