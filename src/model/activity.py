import peewee as pw

from core.model.base import BaseModel
from playhouse.shortcuts import model_to_dict


class Activity(BaseModel):
    name = pw.CharField(null=False)
    url_image = pw.CharField(null=False)

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[Activity.created_at, Activity.updated_at])

    class Meta:
        db_table = "activities"
