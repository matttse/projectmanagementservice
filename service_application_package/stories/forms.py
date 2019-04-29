from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from service_application_package.models import User
from wtforms.validators import DataRequired

class StoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    status = SelectField('Status', choices=[('new','New'), ('in-progress', 'In-Progress'), ('done', 'Done')], validators=[DataRequired()])
    assigned_to = SelectField('Assigned To', validators=[DataRequired()])
    content = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit New Story')
 	def __init__(self, *args, **kwargs):
        super(StoryForm, self).__init__(*args, **kwargs)
        self.assigned_to.choices = [(a.id, a.username) for a in User.query.order_by(User.username)]