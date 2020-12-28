from flask_babel import lazy_gettext as _l
from flask_wtf import FlaskForm
from wtforms import BooleanField, FileField, PasswordField, StringField, SelectField, SubmitField, TextAreaField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, NumberRange


class LoginForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    show_password = BooleanField(_l("Show password"))
    remember = BooleanField(_l("Remember me"))
    submit = SubmitField(_l("Login"))
