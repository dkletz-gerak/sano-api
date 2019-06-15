from src.model import Activity
from src.exception import *
from core.util import *

def get_all_activities():
    query = Activity.select().dicts()
    return respond_data([activity for activity in query])