import peewee as pw

from core.model.base import BaseModel
from src.model.location import Location


class LocationImage(BaseModel):
    url = pw.CharField(null=False)
    location = pw.ForeignKeyField(Location)

    class Meta:
        db_table = "location_images"
