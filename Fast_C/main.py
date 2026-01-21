from fastapi import FastAPI
from route import route
import uvicorn

app = FastAPI()

app.include_router(route)


if __name__ == "__main__":
    uvicorn.run(app,host="localhost",port=8092)