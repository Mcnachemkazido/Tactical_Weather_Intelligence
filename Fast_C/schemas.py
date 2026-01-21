from pydantic import BaseModel
from datetime import datetime

class Location(BaseModel):
    timestamp: datetime
    location_name: str
    country: str
    latitude: float
    longitude: float
    temperature: float
    wind_speed: float
    humidity: int
    temperature_category: str
    wind_category: str


l = Location(timestamp=datetime.now(),location_name="fds",country="sg",latitude=3.4
             ,longitude=5.4 ,temperature=4.3,wind_category="ge",
             humidity=4,temperature_category="fdas",wind_speed=54.4)

m = Location(timestamp=datetime.now(),location_name="ffgds",country="sg",latitude=3.4
             ,longitude=5.4 ,temperature=4.3,wind_category="ge",
             humidity=4,temperature_category="fdasgs",wind_speed=54.444444444444)