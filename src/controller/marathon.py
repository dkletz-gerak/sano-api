from src.model.marathon import Marathon
from core.util import *
from flask import request


def add_marathon():
    preferences = request.json.get("preferences")
    location_id = request.json.get("location_id")
    lat = request.json.get("lat")
    long = request.json.get("long")

    marathon = Marathon(
        preferences=preferences,
        lat=lat,
        long=long,
        location=location_id,
    )
    marathon.save()

    return respond_data(marathon.to_dict(), 201)
