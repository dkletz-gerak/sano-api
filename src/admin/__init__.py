from src.admin.views import *
from src.model import *

views = [
    UserAdmin(User),
    CategoryAdmin(Category),
    LocationAdmin(Location),
    EventAdmin(Event),
    ActivityAdmin(Activity),
    MembershipAdmin(Membership),
    RoutineAdmin(Routine),
    ScheduleAdmin(Schedule),
    LocationImageAdmin(LocationImage),
]
