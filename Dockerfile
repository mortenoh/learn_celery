# Use official Python image with version 3.12
FROM python:3.12-slim

ENV UV_COMPILE_BYTECODE=1
ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

# Speed up pip using uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Create a non-root user
RUN useradd -ms /bin/bash celeryuser

# Set the working directory in the container
WORKDIR /code

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN uv pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code
COPY . .

# Set the user to 'celeryuser'
USER celeryuser

# Expose the FastAPI port
EXPOSE 8000
