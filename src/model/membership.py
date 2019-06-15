from enum import Enum
from core.model.base import BaseModel
from playhouse.shortcuts import model_to_dict
import peewee as pw
from src.model.user import User


class MembershipType(Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"


class Membership(BaseModel):
    name = pw.CharField(null=False)
    member_type = pw.CharField(null=False)
    description = pw.TextField(null=False, default="")
    user = pw.ForeignKeyField(User, backref="membership", unique=True)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "memberships"
