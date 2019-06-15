import peewee as pw

from core.model.base import BaseModel
from src.model import Location
from src.model.activity import Activity


class LocationActivity(BaseModel):
    location = pw.ForeignKeyField(Location, null=False)
    activity = pw.ForeignKeyField(Activity, null=False)
    weight = pw.IntegerField(default=1)

    class Meta:
        db_table = "location_activity"
