from celery.result import AsyncResult
from fastapi import FastAPI
from pydantic import BaseModel

from .celery_worker import celery_app
from .tasks import add

app = FastAPI()


# Define the response model for the add task
class AddResponse(BaseModel):
    message: str
    task_id: str


# Define the response model for the task status
class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    result: str


@app.get("/api/add", response_model=AddResponse)
async def add_numbers(x: int, y: int):
    """
    Trigger a Celery task to add two numbers (x + y).
    """
    task = add.delay(x, y)
    return {"message": f"Task {task.id} is running!", "task_id": task.id}


@app.get("/api/status/{task_id}", response_model=TaskStatusResponse)
async def get_task_status(task_id: str):
    """
    Query the status and result of a Celery task by task_id.
    """
    task_result = AsyncResult(task_id, app=celery_app)

    if task_result.state == "PENDING":
        result = "Task is pending..."
    elif task_result.state == "FAILURE":
        result = str(task_result.result)
    elif task_result.state == "SUCCESS":
        result = str(task_result.result)
    else:
        result = f"Task is {task_result.state}"

    return {"task_id": task_id, "status": task_result.state, "result": result}
