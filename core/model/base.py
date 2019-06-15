from playhouse.shortcuts import model_to_dict
from datetime import datetime
import peewee as pw
from core.database.database import db
import pytz


def datetime_tz():
    return datetime.now(pytz.UTC)


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(default=datetime_tz)
    updated_at = pw.DateTimeField(default=datetime_tz)

    def to_dict(self):
        return model_to_dict(self)

    def save(self, *args, **kwargs):
        self.updated_at = datetime_tz().strftime("%Y-%m-%d %H:%M:%S")
        super().save(*args, **kwargs)

    class Meta:
        database = db
