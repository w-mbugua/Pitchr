from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    post = TextAreaField('Pitch', validators=[DataRequired()])
    submit = SubmitField('Post')
