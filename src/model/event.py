import peewee as pw

from core.model.base import BaseModel
from src.model.location import Location


class Event(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    image = pw.CharField(null=False)
    description = pw.TextField()
    location = pw.ForeignKeyField(Location)
    start_date = pw.DateTimeField()
    end_date = pw.DateTimeField()

    class Meta:
        db_table = "events"
