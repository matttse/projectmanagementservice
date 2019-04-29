from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from service_application_package.models import User
from wtforms.validators import DataRequired

class StoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    status = SelectField('Status', choices=[('new','New'), ('in-progress', 'In-Progress'), ('done', 'Done')], validators=[DataRequired()])
    assigned_to = SelectField('Assigned To', choices=[('matt','Matt'), ('ryan', 'Ryan'), ('peter', 'Peter'), ('kevin', 'Kevin'), ('peng', 'Peng'), ('guanhang', 'Guanhang')],validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit New Story')
