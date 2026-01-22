from fastapi import FastAPI
from route import route
import uvicorn

app = FastAPI()

app.include_router(route)

