from fastapi import APIRouter, FastAPI
from fastapi.encoders import jsonable_encoder
import uvicorn
import requests
from models import ingest_weather_for_location

router = APIRouter()
app = FastAPI(title="Service A")
app.include_router(router)

SERVICE_B_URL = ("http://localhost:8081")

@router.post("/ingest")
def send_to_storage(location: str):
    data = ingest_weather_for_location(location)
    endpoint = f"{SERVICE_B_URL}/clean"
    response = requests.post(endpoint, json=data.model_dump())
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)

