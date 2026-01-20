from datetime import datetime
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
import requests

def fetch_coordinates(location_name: str):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": location_name,
        "count": 1
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    if "results" not in data or not data["results"]:
        raise ValueError(f"Location not found: {location_name}")

    result = data["results"][0]
    return {
        "location_name": result["name"],
        "country": result.get("country"),
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }

def fetch_hourly_weather(latitude: float, longitude: float):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m,wind_speed_10m,relative_humidity_2m",
        "past_days": 1,
        "timezone": "UTC"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["hourly"]

router = APIRouter()
@router.post("/ingest")
def ingest_weather_for_location(location_name):
    records = []

    location = fetch_coordinates(location_name)

    hourly_data = fetch_hourly_weather(
        location["latitude"],
        location["longitude"]
    )

    times = hourly_data["time"]
    temperatures = hourly_data["temperature_2m"]
    wind_speeds = hourly_data["wind_speed_10m"]
    humidities = hourly_data["relative_humidity_2m"]

    for i in range(len(times)):
        record = {
            "timestamp": datetime.fromisoformat(times[i]),
            "location_name": location["location_name"],
            "country": location["country"],
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "temperature": temperatures[i],
            "wind_speed": wind_speeds[i],
            "humidity": humidities[i]

        }
        records.append(record)

    return records

SERVICE_B_URL = ("SERVICE_B_URL", "http://localhost:8081")

def send_to_storage(data):
    endpoint = f"{SERVICE_B_URL}/clean"
    response = requests.post(endpoint, json=data.model_dump())
    json_data = jsonable_encoder(data)
    return json_data