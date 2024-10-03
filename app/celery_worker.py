from celery import Celery

# Create the Celery app instance
celery_app = Celery(
    "tasks",
    broker="redis://redis:6379/0",  # Redis as broker
    backend="redis://redis:6379/0",  # Redis as result backend
    broker_connection_retry_on_startup=True,
)

# Celery Beat schedule
celery_app.conf.update(
    beat_schedule={
        "say-hello-every-30-seconds": {
            "task": "app.tasks.add",
            "schedule": 30.0,  # Run this task every 30 seconds
            "args": (10, 20),
        },
    },
    timezone="UTC",
    beat_scheduler="celery.beat.PersistentScheduler",  # Use persistent scheduler
    beat_schedule_filename="/code/celerybeat-schedule.db",  # Store schedule in a .db file
)

# Auto-discover tasks from the 'app' module
celery_app.autodiscover_tasks(["app"])
