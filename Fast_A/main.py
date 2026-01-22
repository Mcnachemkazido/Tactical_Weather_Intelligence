from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import requests
import uvicorn
from models import ingest_weather_for_location
from dotenv import load_dotenv
import os
load_dotenv()


SERVICE_B_HOST = os.getenv("SERVICE_B_HOST")
endpoint = f"http://{SERVICE_B_HOST}:8091/clean"


app = FastAPI(title="Service A")

@app.post("/ingest")
def send_to_storage(location:str):
    data = ingest_weather_for_location(location)
    json_data = jsonable_encoder(data)
    requests.post(endpoint,json=json_data)
    return {"true":"Successfully sent to server B"}



