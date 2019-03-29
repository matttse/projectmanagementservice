from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class StoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit New Story')
