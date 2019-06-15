from flask import request, jsonify
from src.model.redis.session import Session


def respond_data(data, code=200):
    return jsonify({"status": code, "data": data}), code


def respond_error_message(message, code=500):
    return jsonify({"status": code, "message": message}), code
