from src.exception import *
from core.util import *
from src.model import Schedule


def get_schedule_by_id(schedule_id):
    schedule = Schedule.get_or_none(Schedule.id == schedule_id)
    if schedule is None:
        raise SanoException(404, NOT_FOUND, "Schedule not found")

    return respond_data(schedule.to_dict(True))
