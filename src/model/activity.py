import peewee as pw

from core.model.base import BaseModel


class Activity(BaseModel):
    name = pw.CharField(null=False)
    url_image = pw.CharField(null=False)

    class Meta:
        db_table = "activities"
