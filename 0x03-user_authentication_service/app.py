#!/usr/bin/env python3
"""Defines a simple Flask Application"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """
    Define the home intro for the flask app
    """
    payload = {"message": "Bienvenue"}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
