import peewee as pw
from core.model.base import BaseModel
from src.model.location import Location


class Routine(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    image = pw.CharField(null=False)
    requirements = pw.CharField(null=False)
    description = pw.TextField()
    location = pw.ForeignKeyField(Location, null=False, backref='routines')
    is_stop = pw.BooleanField()

    class Meta:
        db_table = "routines"
