from pydantic import BaseModel
from datetime import datetime

class Location(BaseModel):
    timestamp: datetime | None
    location_name: str | None
    country: str | None
    latitude: float | None
    longitude: float |  None
    temperature: float | None
    wind_speed: float | None
    humidity: int | None
    temperature_category: str | None
    wind_category: str | None

