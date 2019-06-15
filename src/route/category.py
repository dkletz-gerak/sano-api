from src.controller.category import *
from core.router import Router


category_router = Router()
category_router.get("", get_all_categories)
category_router.get("/<int:category_id>", get_category_by_id)
