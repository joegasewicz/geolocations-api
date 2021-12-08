import os
from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mongo_id_marshaller import MongoId
from pydantic import BaseModel
from pymongo import MongoClient

# We want a KeyError if any of these variables are not defined
API_DB_NAME = os.environ["API_DB_NAME"]
API_DB_USERNAME = os.environ["API_DB_USERNAME"]
API_DB_PASSWORD = os.environ["API_DB_PASSWORD"]
API_DB_HOST = os.environ["API_DB_HOST"]
API_DB_PORT = os.environ["API_DB_PORT"]

client = MongoClient(f"mongodb://{API_DB_USERNAME}:{API_DB_PASSWORD}@{API_DB_HOST}:{int(API_DB_PORT)}")
app = FastAPI()
mongo_id = MongoId()

db = client.bn_database

origins = [
    # To restrict access use below examples instead of "*"
    # "http://localhost",
    # "http://localhost:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class Town(BaseModel):
    id: str
    country: str
    county: str
    latitude: float
    loc: List[float]
    longitude: float
    reference: str
    town: str
    type: str


@app.get("/towns", response_model=Town)
def locations(name: str = None):
    if name:
        towns = db["towns"].find({
            "town": {
                "$regex": f"^{name}",
                "$options": "i",
            }},
            {
                "loc": 0,
                "__v": 0,
            }
        ).limit(5)
        serialized_towns = mongo_id.multiple(towns)
        json_data = jsonable_encoder(serialized_towns)
        return JSONResponse(content=json_data)
    else:
        return None
