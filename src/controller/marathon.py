from src.model import Location, Marathon
from src.exception import *
from core.util import *
from flask import request


def add_marathon():
    preferences = request.json.get("preferences")
    location_id = request.json.get("location_id")
    lat = request.json.get("lat")
    long = request.json.get("long")

    location = Location.get_or_none(Location.id == location_id)
    if location is None:
        raise SanoException(404, NOT_FOUND, "location not found")

    marathon = Marathon(
        preferences=preferences,
        lat=lat,
        long=long,
        location=location,
    )
    marathon.save()

    return respond_data(marathon.to_dict(), 201)
