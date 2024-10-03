from .celery_worker import celery_app


@celery_app.task(name="app.tasks.add")
def add(x: int, y: int) -> int:
    result = x + y
    print(f"Doing {x} + {y} = {result}")
    return result
