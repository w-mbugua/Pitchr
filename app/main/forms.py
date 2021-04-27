from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class PitchForm(FlaskForm):
    category = SelectField('Category', validators=[DataRequired()], choices=[(
        'promotion', 'Promotion'), ('product', 'Product'), ('elevator', 'Elevator'), ('pickup', 'Pickup Lines')])
    post = TextAreaField('Pitch', validators=[DataRequired()])
    submit = SubmitField('Post')
   

class CommentForm(FlaskForm):
    content = TextAreaField('Reply', validators=[DataRequired()])
    submit = SubmitField('Post')
