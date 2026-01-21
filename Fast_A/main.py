from fastapi import FastAPI
import requests
import uvicorn
from models import ingest_weather_for_location
from schemas import Location

SERVICE_B_URL = "http://localhost:8081"
endpoint = f"{SERVICE_B_URL}/clean"


app = FastAPI(title="Service A")

@app.post("/ingest")
def send_to_storage(location:Location):
    data = ingest_weather_for_location(location.location)
    requests.post(endpoint,json=data.model_dump())




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)

