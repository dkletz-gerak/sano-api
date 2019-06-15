from flask_admin.contrib.peewee import ModelView
from wtforms import PasswordField, SelectField
from wtforms.validators import Optional
from src.model import *


class UserAdmin(ModelView):
    inline_models = [
        (
            Membership,
            dict(
                form_overrides=dict(member_type=SelectField, ),
                form_args=dict(
                    id=dict(validators=[Optional()]),
                    member_type=dict(
                        choices=[
                            ('bronze', 'bronze'),
                            ('silver', 'silver'),
                            ('gold', 'gold')
                        ]
                    )
                )
            )
        )
    ]

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
    inline_models = [
        (LocationImage, dict(form_args=dict(id=dict(validators=[Optional()])))),
        (LocationActivity, dict(form_args=dict(id=dict(validators=[Optional()])))),
        (Routine, dict(form_args=dict(id=dict(validators=[Optional()])))),
        (Event, dict(form_args=dict(id=dict(validators=[Optional()]))))
    ]


class EventAdmin(ModelView):
    pass


class ActivityAdmin(ModelView):
    inline_models = [(LocationActivity, dict(form_args=dict(id=dict(validators=[Optional()]))))]


class MembershipAdmin(ModelView):
    form_overrides = dict(
        member_type=SelectField,
    )
    form_args = dict(
        member_type=dict(
            choices=[
                ('bronze', 'bronze'),
                ('silver', 'silver'),
                ('gold', 'gold')
            ]
        )
    )


class RoutineAdmin(ModelView):
    inline_models = [(Schedule, dict(form_args=dict(id=dict(validators=[Optional()]))))]


class ScheduleAdmin(ModelView):
    pass


class LocationImageAdmin(ModelView):
    pass
