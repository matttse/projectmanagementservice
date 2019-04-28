from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, validators, SelectField
from wtforms.validators import DataRequired
from service_application_package.models import Project, User, Story
from datetime import datetime

class IssueForm(FlaskForm):
    title = StringField('Issue Title', validators=[DataRequired()])
    issue_description = TextAreaField('Issue Description', validators=[DataRequired()])
    issue_date = DateField('Opened Date', format='%m/%d/%Y', validators=[DataRequired()], default=datetime.today)
    priority = SelectField('Priority', choices = [('nice to do','Nice to do'),('important','Important'),('urgent','Urgent'),('closed','Closed')], validators=[DataRequired()])
    completed_date = DateField('Completed Date', format='%m/%d/%Y', validators=(validators.Optional(),))
    opened_by = SelectField('Opened By', validators=[DataRequired()], coerce=int)
    project = SelectField('Project Name', validators=[DataRequired()], coerce=int)
    story = SelectField("Story Name", validators=[DataRequired()], coerce=int)
    submit = SubmitField('Submit New Issue')

    def __init__(self, *args, **kwargs):
        super(IssueForm, self).__init__(*args, **kwargs)
        self.project.choices = [(a.id, a.title) for a in Project.query.order_by(Project.title)]
        self.story.choices = [(a.id,a.title) for a in Story.query.order_by(Story.title)]
        self.opened_by.choices = [(a.id, a.username) for a in User.query.order_by(User.username)]
