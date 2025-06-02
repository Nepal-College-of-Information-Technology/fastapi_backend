# FastAPI with TinyDB Web Server

This project sets up a simple web server using FastAPI with TinyDB as the database, containerized with Docker and orchestrated using Docker Compose.

## Prerequisites
- Docker
- Docker Compose

## Project Structure
- **Dockerfile:** Defines the Docker image for the FastAPI application.
- **docker-compose.yml:** Configures the service for running the container.
-  **requirements.txt:** Lists Python dependencies (FastAPI, Uvicorn, TinyDB).
- **main.py:** Contains the FastAPI application with GET and POST endpoints.
- **data/:** Directory for persisting TinyDB's JSON database file.

## Setup and Installation
Clone the repository  or create the project files as provided.


## Build and run the application:
```docker-compose up --build```
