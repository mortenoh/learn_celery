from celery import Celery

# Create the Celery app instance
celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",  # Redis as broker
    backend="redis://redis:6379/0",  # Redis as result backend
)

# Celery Beat schedule
celery_app.conf.beat_schedule = {
    "say-hello-every-30-seconds": {
        "task": "app.tasks.add",
        "schedule": 30.0,  # Run this task every 30 seconds
        "args": (10, 20),
    },
}

# Set timezone
celery_app.conf.timezone = "UTC"

# Auto-discover tasks from the 'app' module
celery_app.autodiscover_tasks(["app"])
