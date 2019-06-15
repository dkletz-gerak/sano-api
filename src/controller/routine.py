from src.exception import *
from core.util import *
from flask import request
from src.model import Location, Routine


def get_routines():
    location_id = request.args.get("t")
    if location_id:
        location = Location.get_or_none(Location.id == location_id)
    pass