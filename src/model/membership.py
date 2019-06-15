from enum import Enum

import peewee as pw

from core.model.base import BaseModel
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

    class Meta:
        db_table = "memberships"
