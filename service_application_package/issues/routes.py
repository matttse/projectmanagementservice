from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from service_application_package import db
from service_application_package.models import Issue, Project, User
from service_application_package.issues.forms import IssueForm

issues = Blueprint('issues', __name__)

@issues.route("/issues/all")
def list_issues():
    form = IssueForm()
    issues = Issue.query.all()
    projects = Project.query.all()
    users = User.query.all()
    return render_template('issues_all.html', 
                           form=form, title='issue', legend="New Issue", issues=issues, projects=projects, users=users)

@issues.route("/issue/<int:issue_id>")
def issue(issue_id):
    issue = Issue.query.get_or_404(issue_id)
    return render_template('issue.html', title=issue.title, issue=issue)

@issues.route("/issue/new", methods=['GET', 'POST'])
@login_required
def new_issue():
    form = IssueForm()
    projects = Project.query.all()
    users = User.query.all()
    if form.validate_on_submit():
        issue = Issue(title=form.title.data,
        issue_description=form.issue_description.data,
        issue_date=form.issue_date.data,
        priority=form.priority.data,
        completed_date=form.completed_date.data,
        open_by=form.opened_by.data,
        project=form.project.data)
        db.session.add(issue)
        db.session.commit()
        flash('Your issue has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_issue.html', title='New Issue',
                           form=form, legend='New Issue', projects=projects, users=users)