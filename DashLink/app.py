import json  # Importing the JSON module for handling JSON data
from flask import Flask, render_template, request, redirect, url_for  # Importing required functions and classes from Flask

app = Flask(__name__)  # Initializing a new Flask web application

# Path to the bookmarks file
BOOKMARKS_FILE = "bookmarks.json"  # Define the file path where bookmarks will be stored

# Load bookmarks from the JSON file
def load_bookmarks():
    try:
        # Open the bookmarks file in read mode
        with open(BOOKMARKS_FILE, "r") as file:
            return json.load(file)  # Parse and return the contents of the file as a dictionary
    except (FileNotFoundError, json.JSONDecodeError):
        # If file is not found or JSON is corrupted, return an empty dictionary
        return {}

# Save bookmarks to the JSON file
def save_bookmarks(bookmarks):
    # Open the bookmarks file in write mode
    with open(BOOKMARKS_FILE, "w") as file:
        # Save the bookmarks dictionary as a JSON file with indentation for readability
        json.dump(bookmarks, file, indent=4)

# Initialize the bookmarks by loading them from the JSON file
bookmarks = load_bookmarks()

# Route to handle the homepage, displaying the bookmarks
@app.route('/')
def index():
    return render_template('index.html', bookmarks=bookmarks)  # Render the index.html template and pass the bookmarks data

# Route to handle adding a new category
@app.route('/add_category', methods=['POST'])
def add_category():
    category = request.form['category']  # Get the new category name from the form submission
    if category not in bookmarks:  # Check if the category doesn't already exist
        bookmarks[category] = []  # Create a new empty category
        save_bookmarks(bookmarks)  # Save the updated bookmarks to the JSON file
    return redirect(url_for('index'))  # Redirect the user back to the homepage

# Route to handle adding a new bookmark
@app.route('/add', methods=['POST'])
def add_bookmark():
    category = request.form['category']  # Get the category for the new bookmark
    name = request.form['name']  # Get the name of the new bookmark
    link = request.form['link']  # Get the link for the new bookmark
    if category in bookmarks:  # Check if the category exists
        # Append the new bookmark (name and link) to the list of bookmarks in the selected category
        bookmarks[category].append({'name': name, 'link': link})
        save_bookmarks(bookmarks)  # Save the updated bookmarks to the JSON file
    return redirect(url_for('index'))  # Redirect the user back to the homepage

# Route to handle deleting a bookmark
@app.route('/delete', methods=['POST'])
def delete_bookmark():
    category = request.form['category']  # Get the category of the bookmark to delete
    name = request.form['name']  # Get the name of the bookmark to delete
    if category in bookmarks:  # Check if the category exists
        # Remove the bookmark by filtering out the one with the specified name
        bookmarks[category] = [bm for bm in bookmarks[category] if bm['name'] != name]
        save_bookmarks(bookmarks)  # Save the updated bookmarks to the JSON file
    return redirect(url_for('index'))  # Redirect the user back to the homepage

# Route to handle editing a bookmark
@app.route('/edit', methods=['POST'])
def edit_bookmark():
    category = request.form['category']  # Get the category of the bookmark to edit
    old_name = request.form['old_name']  # Get the current name of the bookmark
    new_name = request.form['new_name']  # Get the new name for the bookmark
    new_link = request.form['new_link']  # Get the new link for the bookmark
    if category in bookmarks:  # Check if the category exists
        # Iterate through the bookmarks in the category and find the one to edit
        for bm in bookmarks[category]:
            if bm['name'] == old_name:
                bm['name'] = new_name  # Update the bookmark name
                bm['link'] = new_link  # Update the bookmark link
        save_bookmarks(bookmarks)  # Save the updated bookmarks to the JSON file
    return redirect(url_for('index'))  # Redirect the user back to the homepage

# Main entry point of the application
if __name__ == '__main__':
    app.run(debug=True, port=5020)  # Run the Flask application in debug mode on port 5020
