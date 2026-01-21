from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
import requests
import uvicorn
from models import ingest_weather_for_location




SERVICE_B_URL = "http://localhost:8081"
endpoint = f"{SERVICE_B_URL}/clean"


app = FastAPI(title="Service A")

@app.post("/ingest")
def send_to_storage(location:str):
    data = ingest_weather_for_location(location)
    json_data = jsonable_encoder(data)
    res = requests.post(endpoint,json=json_data)
    return res.json()




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)

