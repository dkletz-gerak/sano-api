import peewee as pw
from core.model.base import BaseModel


class CoreMigration(BaseModel):
    name = pw.CharField(null=False)
    batch = pw.IntegerField(default=0)

    class Meta:
        db_table = "users"
