#!/usr/bin/python3
"""
This module implements a Flask-based API server with multiple endpoints.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionary to store user data
users = {}


@app.route('/')
def home():
    """Responds with a welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """Returns a JSON list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """Returns the status of the API."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Returns user profile information for the given username."""
    profile = users.get(username)
    if profile:
        return jsonify(profile)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Adds a new user to the users dictionary from a JSON request."""
    user_data = request.get_json()
    username = user_data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
