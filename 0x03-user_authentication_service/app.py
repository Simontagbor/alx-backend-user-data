#!/usr/bin/env python3
"""Defines a simple Flask Application"""

from flask import request, Flask, jsonify
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound

app = Flask(__name__)

AUTH = Auth()


@app.route('/')
def home():
    """
    Define the home intro for the flask app
    """
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


@app.route('/users', methods=['POST'])
def create_user():
    """ this endpoint creates a new user"""
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    email = data.get('email')
    password = data.get('password')
    try:
        AUTH._db.find_user_by(email=email)
        return jsonify({"message": "email already registered"}), 400
    except NoResultFound:
        AUTH.register_user(email, password)
    return jsonify({"email": f"{email}", "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
