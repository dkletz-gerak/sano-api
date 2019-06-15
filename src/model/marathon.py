import peewee as pw
from core.model.base import BaseModel
from src.model.location import Location
from playhouse.shortcuts import model_to_dict


class Marathon(BaseModel):
    preferences = pw.CharField(null=False)
    location = pw.ForeignKeyField(Location, null=False)
    lat = pw.FloatField(null=False)
    long = pw.FloatField(null=False)

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[Marathon.created_at, Marathon.updated_at])

    class Meta:
        db_table = "marathons"
