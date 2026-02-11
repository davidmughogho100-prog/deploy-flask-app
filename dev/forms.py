from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(), Length(min=6, max=36)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=12)])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    full_name = StringField("Full name", validators=[DataRequired(), Length(min=8, max=40)])
    email = StringField("Email", validators=[DataRequired(), Length(min=6, max=36)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=12)])
    c_password = PasswordField("confirm password", validators=[DataRequired(), Length(min=5, max=12)])
    submit = SubmitField("submit")


