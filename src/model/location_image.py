import peewee as pw
from playhouse.shortcuts import model_to_dict
from src.model.location import Location
from core.model.base import BaseModel


class LocationImage(BaseModel):
    url = pw.CharField(null=False)
    location = pw.ForeignKeyField(Location)

    def to_dict(self):
        return model_to_dict(self)
