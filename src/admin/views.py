from flask_admin.contrib.peewee import ModelView
from wtforms import PasswordField, SelectField

from src.model import User


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
