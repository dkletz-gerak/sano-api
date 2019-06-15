from core.router import Router
from src.controller.location import *

location_router = Router()
location_router.get("/<int:event_id>", get_location_by_id) 