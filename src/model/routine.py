import peewee as pw
from playhouse.shortcuts import model_to_dict
from core.model.base import BaseModel
from src.model.location import Location


class Routine(BaseModel):
    name = pw.CharField(max_length=100, null=False)

    requirements = pw.CharField(null=False)
    location = pw.ForeignKeyField(Location, null=False, backref='routines')

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "routines"
