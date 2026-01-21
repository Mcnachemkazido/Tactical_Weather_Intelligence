from fastapi import APIRouter ,HTTPException
from schemas import Location
from data_handling import create_df ,data_analysis_columns
from fastapi.encoders import jsonable_encoder
import requests
from dotenv import load_dotenv
import os
load_dotenv()



route = APIRouter()
SERVICE_C_HOST = os.getenv("SERVICE_C_HOST")
endpoint = f"http://{SERVICE_C_HOST}:8092/records"

@route.post("/clean")
def clean_data(locations:list[Location]):
    locations_dict = [l.model_dump() for l in locations]
    df = create_df(locations_dict)
    big_df = data_analysis_columns(df)
    locations_json = big_df.to_dict('records')
    json_data = jsonable_encoder(locations_json)
    requests.post(endpoint, json=json_data)
    return {"true":"Successfully sent to server C"}

