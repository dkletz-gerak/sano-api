from flask import g
from core.middleware import Middleware
from src.exception import *
from src.model.user import UserRole


ACCEPTED_ROLES = [UserRole.ADMIN, UserRole.USER, UserRole.DEVELOPER]


class RoleCheckerMiddleware(Middleware):
    def __init__(self, *args: UserRole):
        super().__init__()
        for arg in args:
            if arg not in ACCEPTED_ROLES:
                raise Exception("Role not found in ACCEPTED_ROLES")

        self.roles = [arg.value for arg in args]

    def pre_check(self, *args, **kwargs):
        if g.user is None:
            return False

        return g.user["role"] in self.roles

    def default(self):
        raise BotMartException(401, NOT_AUTHORIZED, "Not authorized")
