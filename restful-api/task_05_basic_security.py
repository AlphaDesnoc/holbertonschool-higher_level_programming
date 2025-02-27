#!/usr/bin/python3
"""
This module implements a Flask-based API server with
    authentication and security features.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'secret_key'
jwt = JWTManager(app)

# Dictionary to store user data with authentication details
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verifies the provided username and password."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route('/')
def home():
    """Responds with a welcome message for the API."""
    return "Welcome to the Flask API!"


@app.route("/login", methods=['POST'])
def login():
    """Handles user login and returns a JWT token if credentials are valid."""
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    cur_user = users.get(username)
    if cur_user and check_password_hash(cur_user['password'], password):
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    return jsonify({"message": "Bad username or password"}), 401


@app.route("/basic-protected", methods=['GET'])
@auth.login_required
def basic_protected():
    """Endpoint protected by basic authentication."""
    return "Basic Auth: Access Granted"


@app.route("/jwt-protected", methods=['GET'])
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=['GET'])
@jwt_required()
def admin():
    """Endpoint accessible only by admin users."""
    cur_user = get_jwt_identity()
    user = users.get(cur_user)

    if user['role'] == "admin":
        return "Admin Access: Granted"
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    # Run the Flask app in debug mode
    app.run(debug=True)
