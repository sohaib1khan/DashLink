#!/bin/bash

# Define the Flask app file and the port number
APP_FILE="app.py"  # Ensure the app.py file is the correct Flask app file
PORT=5020

# Step 1: Install required libraries
echo "Installing required Python libraries..."
pip install flask

# Step 2: Export the FLASK_APP environment variable (if needed)
export FLASK_APP=$APP_FILE

# Step 3: Launch the Flask app in detached mode using nohup
echo "Starting the Flask app in detached mode..."
nohup flask run --host=0.0.0.0 --port=$PORT > flask_output.log 2>&1 &

# Step 4: Display the access address
IP_ADDRESS=$(hostname -I | awk '{print $1}')  # Get the local IP address
echo "The app is running and can be accessed at: http://$IP_ADDRESS:$PORT"

# Exit the script
exit 0
