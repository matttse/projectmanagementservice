from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField, validators
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from service_application_package.models import Project

class IssueForm(FlaskForm):
    title = StringField('Issue Title', validators=[DataRequired()])
    issue_description = TextAreaField('Issue Description', validators=[DataRequired()])
    priority = TextAreaField('Issue Description', validators=[DataRequired()])
    completed_date = DateField('Completed Date', format='%m/%d/%Y', validators=(validators.Optional(),))
    
    submit = SubmitField('Submit New Issue')