from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, validators, SelectField
from wtforms.validators import DataRequired
from service_application_package.models import Project, User
import time

class IssueForm(FlaskForm):
    title = StringField('Issue Title', validators=[DataRequired()])
    issue_description = TextAreaField('Issue Description', validators=[DataRequired()])
    issue_date = DateField('Issue Date', format='%m/%d/%Y', validators=[DataRequired()], default=time.strftime('%m/%d/%Y'))
    priority = TextAreaField('Priority', validators=[DataRequired()])
    completed_date = DateField('Completed Date', format='%m/%d/%Y', validators=(validators.Optional(),))
    opened_by = SelectField('Opened By', validators=[DataRequired()])
    project = SelectField('Project Name', validators=[DataRequired()])
    submit = SubmitField('Submit New Issue')

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.project.choices = [(a.id, a.title) for a in Project.query.order_by(Project.title)]
        self.opened_by.choices = [(a.id, a.username) for a in User.query.order_by(User.username)]