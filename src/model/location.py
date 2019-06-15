import peewee as pw

from core.model.base import BaseModel
from src.model.category import Category


class Location(BaseModel):
    name = pw.CharField(null=False)
    logo = pw.CharField(null=False)
    address = pw.CharField(null=False)
    lat = pw.FloatField(null=False)
    long = pw.FloatField(null=False)
    category = pw.ForeignKeyField(Category)

    class Meta:
        db_table = "locations"
