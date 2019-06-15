import peewee as pw

from core.model.base import BaseModel
from src.model.location import Location
from playhouse.shortcuts import model_to_dict


class LocationImage(BaseModel):
    url = pw.CharField(null=False)
    location = pw.ForeignKeyField(Location, backref="images")

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[LocationImage.created_at, LocationImage.updated_at])

    class Meta:
        db_table = "location_images"
