from src.controller.activity import *
from core.router import Router

activity_router = Router()
activity_router.get("", get_all_activities)