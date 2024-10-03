import time

from .celery_worker import celery_app


@celery_app.task(name="app.tasks.add")
def add(x: int, y: int) -> int:
    print(f"Doing {x} + {y}")
    time.sleep(10)
    result = x + y
    print(f"Result = {result}")
    return result
