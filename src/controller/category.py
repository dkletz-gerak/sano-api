from src.model import Category
from src.exception import *
from core.util import *


def get_all_categories():
    categories = Category.select().get().dicts()
    return respond_data(categories)


def get_category_by_id(category_id):
    category = Category.get_or_none(Category.id == category_id)
    if category is None:
        raise SanoException(404, NOT_FOUND, "Category not found")

    return respond_data(category.to_dict())
