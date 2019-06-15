import peewee as pw
from core.model.base import BaseModel
from src.model.location import Location
from playhouse.shortcuts import model_to_dict


class Event(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    description = pw.TextField()
    location = pw.ForeignKeyField(Location)
    start_date = pw.DateTimeField()
    end_date = pw.DateTimeField()

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "events"
