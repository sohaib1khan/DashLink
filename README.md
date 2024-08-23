# Bookmarks Dashboard

A simple Flask-based web application that allows users to manage their bookmarks by adding, editing, and deleting bookmarks within categorized sections. The application stores bookmarks in a JSON file (`bookmarks.json`), making it lightweight and easy to run.

## Features

- Add, edit, and delete bookmark categories
- Add, edit, and delete bookmarks within categories
- User-friendly web interface
- Lightweight JSON storage

## Prerequisites

- Python 3.x
- Flask
- Bash (to run the setup script)

## Setup and Installation

Follow these steps to install and run the app:

### Step 1: Clone the Repository

Clone the project repository to your local machine:

### Step 2: Install Dependencies

Use the provided bash script (run_setup.sh) to install required dependencies and launch the app in detached mode. The script uses pip (not pip3), so ensure it's available in your environment.

```
bash run_setup.sh

```
This script will:

- Install the required libraries using `pip`
- Launch the app in detached mode (allowing you to continue using the terminal)
- Display the access address where the app can be reached

### Step 3: Access the Application

Once the script finishes running, you’ll see a message showing the URL where the app can be accessed. It should look something like this:

```
The app is running and can be accessed at: http://<your-local-ip>:5020

```

Open your browser and navigate to this URL.

```
.  
├── app.py # Main Flask application  
├── bookmarks.json # JSON file to store bookmarks data  
├── templates/ # Directory containing HTML templates  
│ └── index.html # Main template file  
├── run_setup.sh # Bash script to install dependencies and launch app  
└── README.md # Project documentation
```


- **`app.py`**: Contains the main Flask application logic for handling routes and bookmark management.
- **`bookmarks.json`**: Stores all the bookmark data in JSON format.
- **`templates/index.html`**: HTML file that defines the front-end interface for managing bookmarks.
- **`run_setup.sh`**: A bash script that sets up the project environment and launches the Flask app in detached mode.

## How to Use

- **Add Category**: Click the "Add Category" button, input the category name, and click submit.
- **Add Bookmark**: Choose a category, input the bookmark name and link, and click submit.
- **Edit Bookmark**: Select the category, choose the bookmark to edit, and update its name or link.
- **Delete Bookmark**: Select the category and the bookmark to delete.

## Customization

- **Themes/Styling**: You can update the `index.html` file in the `templates` folder to change the look and feel of the dashboard.
- **Port**: If you'd like to run the app on a different port, update the `PORT` variable in the `run_setup.sh` script.


## Demo 
![Demo of DashLink](demo_dash.gif)
