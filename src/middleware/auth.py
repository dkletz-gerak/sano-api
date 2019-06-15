from flask import request, g
from core.middleware import Middleware
from src.model.redis.session import Session
from src.exception import *


class AuthMiddleware(Middleware):
    def __init__(self):
        super().__init__()

    def pre_check(self, *args, **kwargs):
        access_token = request.headers.get("Authorization")

        if access_token is None or access_token == "":
            self.default()

        session = Session(access_token)
        session.load()
        g.user = session.data
        g.access_token = access_token

        return g.user is not None

    def default(self):
        raise SanoException(401, NOT_AUTHORIZED, "Not authorized")
