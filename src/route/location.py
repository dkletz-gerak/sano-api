from core.router import Router
from src.controller.location import *
from src.controller.marathon import *


location_router = Router()
location_router.post("/marathon", add_marathon)
location_router.get("/<int:location_id>", get_location_by_id)
location_router.get("/search", search_location)
