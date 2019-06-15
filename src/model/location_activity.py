import peewee as pw
from playhouse.shortcuts import model_to_dict

from core.model.base import BaseModel
from src.model import Location
from src.model.activity import Activity


class LocationActivity(BaseModel):
    location = pw.ForeignKeyField(Location, null=False, backref="activities")
    activity = pw.ForeignKeyField(Activity, null=False)
    weight = pw.IntegerField(default=1)

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[LocationActivity.updated_at, LocationActivity.created_at])

    class Meta:
        db_table = "location_activity"
