from core.model.base import BaseModel
from playhouse.shortcuts import model_to_dict
import peewee as pw


class Activity(BaseModel):
    name = pw.CharField(null=False)

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "activities"
