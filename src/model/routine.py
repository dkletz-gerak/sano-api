import peewee as pw
from core.model.base import BaseModel

class Routine(BaseModel):
    name = pw.CharField(max_length=100, null=False)