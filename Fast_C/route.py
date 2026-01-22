from fastapi import APIRouter
from db.operations import Operations
from schemas import Location

route = APIRouter()


@route.post("/records")
def create_records(locations: list[Location]):
    location_dict = [l.model_dump() for l in locations]
    Operations.insert_to_db(location_dict)
    return {"message": "Data inserted successfully", "count": len(locations)}


@route.get("/get_all")
def get_all():
    return {"data": Operations.select_all()}
