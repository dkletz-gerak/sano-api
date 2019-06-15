from secrets import token_urlsafe
from core.util import *
from src.exception import *
from src.model.user import User, UserRole
from src.model.redis.session import Session
from flask import request, g


def _save_session(access_token: str, user_data: dict):
    session = Session(access_token, user_data)
    session.save()


def register():
    user_data = request.json
    user_data["password"] = User.hash_password(user_data["password"].encode("utf-8"))
    user_data["role"] = UserRole.USER.value

    user = User.get_or_none(User.email == user_data.get("email"))
    if user:
        raise SanoException(400, REGISTER_EXCEPTION, "already registered")

    user = User(**user_data)
    user.save()

    access_token = token_urlsafe(40)

    data = user.to_session_dict()
    _save_session(access_token, data)
    data["access_token"] = access_token

    return respond_data(data, 201)


def login():
    email = request.json.get("email")
    password = request.json.get("password")

    user = User.get_or_none(User.email == email)

    if not user or not user.check_password(password):
        raise SanoException(400, LOGIN_EXCEPTION, "Wrong email/password")

    access_token = token_urlsafe(40)

    data = user.to_session_dict()
    _save_session(access_token, data)
    data["access_token"] = access_token

    return respond_data(data)


def get_profile():
    user = g.user
    user = User.get_or_none(User.id == user["id"])

    return respond_data(user.to_dict())
