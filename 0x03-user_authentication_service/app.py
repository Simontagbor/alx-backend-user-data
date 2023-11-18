#!/usr/bin/env python3
"""Defines a simple Flask Application"""

from flask import request, Flask, jsonify, make_response, abort
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


@app.route('/sessions', methods=['POST'])
def login():
    """log user in and set session id

    Return:
        A json response object
    """
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    email = data.get('email')
    password = data.get('password')
    try:
        user = AUTH._db.find_user_by(email=email)
        if AUTH.valid_login(email, password):
            session_id = AUTH.create_session(email)
            payload = {"email": f"{email}", "message": "logged in"}
            response = make_response(str(payload))
            response.set_cookie('session_id', session_id)
            return response, 200
        else:
            print("email or password wrong")
            abort(401)
    except NoResultFound:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
