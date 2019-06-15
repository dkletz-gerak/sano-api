import peewee as pw

from core.model.base import BaseModel
from src.model.category import Category
from playhouse.shortcuts import model_to_dict


class Location(BaseModel):
    name = pw.CharField(null=False)
    logo = pw.CharField(null=False)
    address = pw.CharField(null=False)
    lat = pw.FloatField(null=False)
    long = pw.FloatField(null=False)
    category = pw.ForeignKeyField(Category)
    price = pw.IntegerField(default=0)

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[Location.created_at, Location.updated_at])

    class Meta:
        db_table = "locations"
