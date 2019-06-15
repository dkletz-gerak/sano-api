from core.router import Router
from src.controller.event import *

event_router = Router()
event_router.get("", get_available_events)
event_router.get("/<int:event_id>", get_event_by_id)
