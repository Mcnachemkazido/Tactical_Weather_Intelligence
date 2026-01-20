from pydantic import BaseModel

class Weather(BaseModel):
    timestamp:
    location_name:
    country:
    latitude:
    longitude:
    temperature:
    wind_speed:
    humidity: