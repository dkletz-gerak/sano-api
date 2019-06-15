from peewee import fn

import math
from core.util import *
from src.exception import *
from src.model import Location, LocationActivity, Activity, Category, Schedule
from datetime import datetime


def get_location_by_id(location_id):
    location = Location.get_or_none(Location.id == location_id)
    if location is None:
        raise SanoException(404, NOT_FOUND, "Location not found")

    location_activities = LocationActivity.select().where(LocationActivity.location == location)
    location_activities = [location_activity.activity_id for location_activity in location_activities]

    activities = Activity.select().where(Activity.id.in_(location_activities))
    activities = [activity.name for activity in activities]

    now = datetime.now()

    data = location.to_dict(recurse=True)
    data["activities"] = activities
    data["images"] = [image.to_dict() for image in location.images]
    data["events"] = [
        event.to_dict() for event in location.events if event.end_date > now
    ]
    data["routines"] = [routine.to_dict() for routine in location.routines if not routine.is_stop]
    for routine in data["routines"]:
        routine["schedules"] = [schedule.to_dict() for schedule in Schedule.select().where(Schedule.routine == routine["id"])]

    return respond_data(data)


def _calculate_weight(delta_lat, delta_long, weight):
    return math.sqrt(delta_lat ** 2 + delta_long ** 2) / weight


def search_location():
    lat = request.args.get("lat")
    long = request.args.get("long")
    preferences = request.args.get("preferences")
    if preferences is None:
        preferences = []
    else:
        preferences = preferences.split(",")

    if len(preferences) > 0:
        query = Activity.select().where(Activity.id.in_(preferences))
    else:
        query = Activity.select()
    activities_query = [activity.to_dict()["id"] for activity in query]

    query = Location.select(Location, Category.name.alias("category_name"),
                            fn.SUM(LocationActivity.weight).alias('weight')) \
                    .join(LocationActivity) \
                    .join(Category, on=Category.id == Location.category) \
                    .where(LocationActivity.activity.in_(activities_query)) \
                    .group_by(Location)

    locations = []
    for location in query.namedtuples():
        weight = location.weight

        if weight == 0:
            weight = 1
        elif len(preferences) == 0:
            weight = 1

        activities = Activity.select().join(LocationActivity).where(LocationActivity.location == location.id)

        locations.append(
            dict(
                name=location.name,
                logo=location.logo,
                address=location.address,
                category=location.category_name,
                normal_weight=weight,
                calculated_weight=_calculate_weight(location.lat-float(lat), location.long-float(long), weight),
                activities=[activity.name for activity in activities],
                price=location.price
            )
        )

    locations.sort(key=lambda object: object["calculated_weight"])

    return respond_data(locations)
