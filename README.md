# Simple docker based Celery/Beat demo

You should have `uv` installed.

## Install

```
uv venv && uv pip install -r requirements.txt
docker compose build && docker compose up
```

## API

```
/api/add?x=10&y=20
/api/status/{task_id}
```
