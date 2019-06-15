from core.model.base import BaseModel
from playhouse.shortcuts import model_to_dict
import peewee as pw
from src.model import Location
from src.model.activity import Activity


class LocationActivity(BaseModel):
    location = pw.ForeignKeyField(Location, null=False)
    activity = pw.ForeignKeyField(Activity, null=False)
    weight = pw.IntegerField(default=1)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "location_activity"
