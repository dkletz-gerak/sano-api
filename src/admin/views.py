from flask_admin.contrib.peewee import ModelView
from wtforms import PasswordField, SelectField
from src.model import *


class UserAdmin(ModelView):
    column_exclude_list = ["password"]
    form_overrides = dict(
        role=SelectField,
        password=PasswordField
    )
    form_args = dict(
        role=dict(
            choices=[
                ('admin', 'admin'),
                ('user', 'user')
            ]
        )
    )

    def on_model_change(self, form, model, is_created):
        if form.password.data:
            model.password = User.hash_password(form.password.data.encode("utf-8"))


class CategoryAdmin(ModelView):
    pass


class LocationAdmin(ModelView):
    inline_models = (LocationImage, LocationActivity, Routine, Event)


class EventAdmin(ModelView):
    pass


class ActivityAdmin(ModelView):
    inline_models = (LocationActivity, )


class MembershipAdmin(ModelView):
    pass


class RoutineAdmin(ModelView):
    inline_models = (Schedule, )


class ScheduleAdmin(ModelView):
    pass
