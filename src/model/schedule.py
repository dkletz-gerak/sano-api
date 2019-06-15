import peewee as pw
from playhouse.shortcuts import model_to_dict
from core.model.base import BaseModel
from src.model.routine import Routine


class Schedule(BaseModel):
    day = pw.IntegerField()
    start_at = pw.CharField()
    end_at = pw.CharField()
    routine = pw.ForeignKeyField(Routine, null=False, backref='schedules')

    def to_dict(self):
        return model_to_dict(self)

    class Meta:
        db_table = "schedules"
