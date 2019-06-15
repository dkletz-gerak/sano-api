from src.exception import *
from core.util import *
from src.model import Location


def get_location_by_id(location_id):
    location = Location.get_or_none(Location.id == location_id)
    if location is None:
        raise SanoException(404, NOT_FOUND, "Location not found")

    return respond_data(location.to_dict(True))


# TODO: our most important feature!!!!
def search_location():
    pass
