from fastapi import FastAPI
import uvicorn
from route import route
app = FastAPI()

app.include_router(route)

