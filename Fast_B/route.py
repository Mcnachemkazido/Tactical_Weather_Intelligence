from fastapi import APIRouter ,HTTPException

route = APIRouter()

@route.post("/clean")
def clean_data():
