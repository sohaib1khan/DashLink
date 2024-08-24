#!/bin/bash

# Define variables for flexibility
APP_NAME="dashlinkapp"  # Name for the Docker container and image
APP_DIR="$(pwd)/DashLink"  # Correctly set the app directory 
PORT=5022  # Port number for the Flask app
COMPOSE_FILE="docker-compose.yml"  # Docker Compose file name

# Step 1: Check if Docker is installed
if ! [ -x "$(command -v docker)" ]; then
  echo 'Error: Docker is not installed.' >&2
  exit 1
fi

# Step 2: Create a Dockerfile if it doesn't exist
if [ ! -f "Dockerfile" ]; then
  echo "Creating Dockerfile..."
  cat <<EOF > Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Install the necessary Python packages (Flask in this case)
RUN pip install flask

# Copy the current directory contents into the container at /app
COPY . /app

# Make port $PORT available to the world outside this container
EXPOSE $PORT

# Define environment variable to avoid buffering in logs
ENV PYTHONUNBUFFERED=1

# Run app.py when the container launches
CMD ["python", "app.py"]
EOF
  echo "Dockerfile created."
fi

# Step 3: Create docker-compose.yml if it doesn't exist
if [ ! -f "$COMPOSE_FILE" ]; then
  echo "Creating docker-compose.yml..."
  cat <<EOF > $COMPOSE_FILE
version: '3'

services:
  $APP_NAME:
    build: .
    ports:
      - "$PORT:$PORT"
    volumes:
      - $APP_DIR:/app
    environment:
      - FLASK_ENV=development
    command: flask run --host=0.0.0.0 --port=$PORT
    restart: always
EOF
  echo "docker-compose.yml created."
fi

# Step 4: Build the Docker image
echo "Building the Docker image..."
docker-compose build

# Step 5: Start the application in detached mode
echo "Starting the Flask app using Docker Compose in detached mode..."
docker-compose up -d

# Step 6: Get the local IP address and display access address
IP_ADDRESS=$(hostname -I | awk '{print $1}')
echo "The app is running and can be accessed at: http://$IP_ADDRESS:$PORT"

