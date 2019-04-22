from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from service_application_package import db
from service_application_package.models import Issue, Project, User
from service_application_package.issues.forms import IssueForm


issues = Blueprint('issues', __name__)

# 
# Issues
# 
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
        project_id=form.project.data)
        db.session.add(issue)
        db.session.commit()
        flash('Your issue has been created!', 'success')
        return redirect(url_for('issues.list_issues'))
    return render_template('create_issue.html', title='New Issue',
                           form=form, legend='New Issue', projects=projects, users=users)

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

@issues.route("/issues/<int:issue_id>/update", methods=['GET', 'POST'])
@login_required
def update_issue(issue_id):
    issue = Issue.query.get_or_404(issue_id)
    form = IssueForm()
    if form.validate_on_submit():
        issue.title=form.title.data
        issue.issue_description=form.issue_description.data
        issue.issue_date=form.issue_date.data
        issue.priority=form.priority.data
        issue.completed_date=form.completed_date.data
        issue.open_by=form.opened_by.data
        issue.project_id=form.project.data
        db.session.commit()
        flash('Your issue has been updated!', 'success')
        return redirect(url_for('issues.list_issues', issue_id=issue.id))
    elif request.method == 'GET':
        form.title.data = issue.title
        form.issue_description.data = issue.issue_description
        form.issue_date.data = issue.issue_date
        form.priority.data = issue.priority
        form.completed_date.data = issue.completed_date
        form.opened_by.data = issue.open_by
        form.project.data = issue.project_id
    return render_template('create_issue.html', title='Update issue',
                           form=form, legend='Update issue')

@issues.route("/issues/Search/")
def issue_search():
    form = IssueForm()
    search_content = request.args.get("Search")
    issues = Issue.query.filter(Issue.title.contains(search_content)).all()
    projects = Project.query.all()
    users = User.query.all()
    if issues:
        return render_template('issues_all.html',  form=form, title='issue', legend="New Issue", issues=issues, projects=projects, users=users)
    else:
        flash('Keyword Not Found', 'danger')
        url_list = url_for('issues.list_issues')
        return redirect(url_list)

@issues.route("/issues/<int:issue_id>/delete", methods=['POST'])
@login_required
def delete_issue(issue_id):
    issue = Issue.query.filter_by(id=issue_id).first()
    db.session.delete(issue)
    db.session.commit()
    flash('Your issue has been deleted!', 'success')
    return redirect(url_for('issues.list_issues', issue_id=issue_id))