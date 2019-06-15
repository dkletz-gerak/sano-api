import peewee as pw
from playhouse.shortcuts import model_to_dict

from core.model.base import BaseModel
from src.model.location import Location


class Event(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    image = pw.CharField(null=False)
    description = pw.TextField()
    location = pw.ForeignKeyField(Location, backref='events')
    start_date = pw.DateTimeField()
    end_date = pw.DateTimeField()
    price = pw.IntegerField(default=0)

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[Event.created_at, Event.updated_at])

    class Meta:
        db_table = "events"
