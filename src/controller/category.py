from src.model import Category
from src.exception import *
from core.util import *


def get_all_categories():
    query = Category.select().dicts()
    return respond_data([category for category in query])


def get_category_by_id(category_id):
    category = Category.get_or_none(Category.id == category_id)
    if category is None:
        raise SanoException(404, NOT_FOUND, "Category not found")

    return respond_data(category.to_dict())
