import peewee as pw

from core.model.base import BaseModel


class Category(BaseModel):
    name = pw.CharField(null=False)
    url_image = pw.CharField(null=False)

    class Meta:
        db_table = "categories"
