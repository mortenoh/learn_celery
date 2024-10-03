from fastapi import FastAPI
from pydantic import BaseModel

from .tasks import add

app = FastAPI()


# Define the response model using Pydantic
class HelloResponse(BaseModel):
    message: str


@app.get("/hello", response_model=HelloResponse)
async def hello():
    # Trigger the Celery task asynchronously
    add.delay(1, 2)
    return {"message": "Hello, FastAPI with Celery!"}
