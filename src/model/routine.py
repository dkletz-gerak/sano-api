import peewee as pw
from core.model.base import BaseModel
from src.model.location import Location
from playhouse.shortcuts import model_to_dict


class Routine(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    image = pw.CharField(null=False)
    requirements = pw.CharField(null=False)
    description = pw.TextField()
    location = pw.ForeignKeyField(Location, null=False, backref='routines')
    is_stop = pw.BooleanField()

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[Routine.created_at, Routine.updated_at])

    class Meta:
        db_table = "routines"
