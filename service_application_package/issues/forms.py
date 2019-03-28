from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, validators
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from service_application_package.models import Project, User

def getUsers():
	return User.query.all()

def project_ids():
	return Project.query.all()

class IssueForm(FlaskForm):
    title = StringField('Issue Title', validators=[DataRequired()])
    issue_description = TextAreaField('Issue Description', validators=[DataRequired()])
    issue_date = DateField(u'date create')
    priority = TextAreaField('Priority', validators=[DataRequired()])
    completed_date = DateField('Completed Date', format='%m/%d/%Y', validators=(validators.Optional(),))
    open_by = TextAreaField('Opened By', validators=[DataRequired()])
    project = QuerySelectField("ProjectID", query_factory=project_ids, allow_blank=False)
    submit = SubmitField('Submit New Issue')

