from fastapi import APIRouter
from db.connection import Connection
from db.operations import Operations
from schemas import Location

route = APIRouter()
@route.post("/records")
def crate_records(locations:list[Location]):
    Connection().crate_db()
    Connection().create_table()
    location_dict = [l.model_dump() for l in locations]
    Operations.insert_to_db(location_dict)
    return {True:True}

@route.get("/get_all")
def get_all():
    return {True: Operations.select_all()}


