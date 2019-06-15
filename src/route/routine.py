from core.router import Router
from src.controller.routine import *

routine_router = Router()
routine_router.get("", get_routines)
routine_router.get("/<int:routine_id>", get_routine_by_id)
