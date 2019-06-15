from src.controller.location import *
from core.router import Router


location_router = Router()
location_router.get("/<int:location_id>", get_location_by_id)
location_router.get("/search", search_location)
