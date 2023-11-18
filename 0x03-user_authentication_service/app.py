#!/usr/bin/env python3
"""Defines a simple Flask Application"""

from flask import request
from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import redirect
from flask import url_for
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
            response = make_response(payload)
            response.set_cookie('session_id', session_id)
            return response, 200
        else:
            abort(401)
    except NoResultFound:
        abort(401)


@app.route('/sessions', methods=['DELETE'])
def logout(self, session_id: str):
    """Log user out
    Arg:
        session_id(str)
    Return:
        None
    """
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form
    session_id = data.get('session_id')
    response = make_response()
    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user.id)
        return redirect(url_for('home'))
    except NoResultFound:
        return response, 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
