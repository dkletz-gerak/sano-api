import peewee as pw
from playhouse.shortcuts import model_to_dict

from core.model.base import BaseModel


class Category(BaseModel):
    name = pw.CharField(null=False)
    url_image = pw.CharField(null=False)

    def to_dict(self, recurse=False, backrefs=False):
        return model_to_dict(self, recurse=recurse, backrefs=backrefs, exclude=[Category.updated_at, Category.created_at])

    class Meta:
        db_table = "categories"
