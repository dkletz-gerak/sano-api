from core.router import Router
from src.controller.schedule import *

schedule_router = Router()
schedule_router.get("/<int:schedule_id>", get_schedule_by_id)
