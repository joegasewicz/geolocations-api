from typing import List
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mongo_id_marshaller import MongoId
from pydantic import BaseModel
from pymongo import MongoClient


client = MongoClient("mongodb://admin:admin@localhost:27017")
app = FastAPI()
mongo_id = MongoId()

db = client.bn_database

origins = [
    "http://localhost:8080",
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
