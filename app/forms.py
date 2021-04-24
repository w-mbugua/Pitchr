from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo

class RegistrationForm:
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm:
    email = StringField('Email', validators=[DataRequired(),  Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')