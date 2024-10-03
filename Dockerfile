# Use official Python image with version 3.12
FROM python:3.12-slim

ENV UV_COMPILE_BYTECODE=1
ENV UV_SYSTEM_PYTHON=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY requirements.txt .
RUN uv pip install --no-cache-dir -r requirements.txt
COPY . /app

RUN useradd -ms /bin/bash celeryuser
USER celeryuser
EXPOSE 8000
