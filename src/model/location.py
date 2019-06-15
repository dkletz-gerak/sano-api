from core.model.base import BaseModel
from playhouse.shortcuts import model_to_dict
import peewee as pw


class Location(BaseModel):
    name = pw.CharField(null=False)
    logo = pw.CharField(null=False)
    address = pw.CharField(null=False)
    lat = pw.FloatField(null=False)
    long = pw.FloatField(null=False)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "locations"
