import peewee as pw
from core.model.base import BaseModel

class Event(BaseModel):
    name = pw.CharField(max_length=100, null=False)
    description = pw.TextField()
    start_date = pw.DateTimeField()
    end_date = pw.DateTimeField()
