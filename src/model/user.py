from enum import Enum
from core.model.base import BaseModel
from playhouse.shortcuts import model_to_dict
import peewee as pw
import bcrypt


class UserRole(Enum):
    ADMIN = "admin"
    USER = "user"

    def __repr__(self):
        return


class User(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    email = pw.CharField(max_length=100, null=False)
    password = pw.CharField(null=False)
    role = pw.CharField(null=False)

    def to_session_dict(self):
        return model_to_dict(
            self, exclude=[User.password, User.created_at, User.updated_at]
        )

    def to_dict(self):
        return model_to_dict(self, exclude=[User.password])

    def check_password(self, password: str):
        return bcrypt.checkpw(
            password.encode("utf-8"), self.password.__str__().encode("utf-8")
        )

    @classmethod
    def hash_password(cls, password):
        return bcrypt.hashpw(password, bcrypt.gensalt(12))

    class Meta:
        db_table = "users"
