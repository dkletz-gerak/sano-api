from src.exception import *
from core.util import *
from src.model import Event, Location
from datetime import datetime
import pytz


def get_available_events():
    location_id = request.args.get("t")
    query_option = (Event.end_date > datetime.now(pytz.UTC))

    if location_id:
        location = Location.get_or_none(Location.id == location_id)
        if location is None:
            raise SanoException(404, NOT_FOUND, "Location not found")

        query_option = query_option & (Event.location == location)

    events = Event.select().where(query_option)

    return respond_data([event.to_dict() for event in events])


def get_event_by_id(event_id):
    event = Event.get_or_none(Event.id == event_id)
    if event is None:
        raise SanoException(404, NOT_FOUND, "Event not found")

    return respond_data(event.to_dict(True))
