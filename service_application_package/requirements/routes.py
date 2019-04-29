from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from service_application_package import db
from service_application_package.models import Requirement
from service_application_package.models import Story
from service_application_package.requirements.forms import RequirementForm
import math

requirements = Blueprint('requirements', __name__)


# 
# Requirements
# 
@requirements.route("/projects/<int:project_id>/requirements/new", methods=['GET', 'POST'])
@login_required
def new_requirement(project_id):
    form = RequirementForm()
    if form.validate_on_submit():
        requirement = Requirement(title=form.title.data, content=form.content.data, project_id=project_id)
        db.session.add(requirement)
        db.session.commit()
        flash('Your requirement has been created!', 'success')
        return redirect(url_for('requirements.list_requirements', project_id=project_id))
    return render_template('create_requirement.html', title='New requirement',
                           form=form, legend='New requirement')


@requirements.route("/projects/<int:project_id>/requirement/<int:requirement_id>")
def requirement(project_id, requirement_id):
    requirement = Requirement.query.get_or_404(requirement_id)
    return render_template('requirements.html', title=requirement.title, requirement=requirement, project_id=project_id)

@requirements.route("/projects/<int:project_id>/requirements/all")
def list_requirements(project_id):
    form = RequirementForm()
    requirement_count = Requirement.query.filter_by(project_id=project_id).count()
    doneList = []
    doneCount = 0
    total = 0
    if requirement_count > 0:
        requirements = Requirement.query.filter_by(project_id=project_id)

        for id1, req in enumerate(requirements):
            stories = Story.query.filter_by(requirement_id=req.id)
            for id2, sto in enumerate(stories):
                if sto.status == 'done':
                    doneCount += 1
                total += 1
            if(total == 0):
                doneList.append(0)
            else:
                percentDone = (doneCount / total) * 100
                doneList.append(math.ceil(percentDone))
            doneCount = 0
            total = 0
    else:
        requirements = 0

    return render_template('requirements.html', 
                           form=form, title='requirement', legend="New requirement", requirements=requirements, project_id=project_id, doneList = doneList )

@requirements.route("/projects/<int:project_id>/requirements/<int:requirement_id>", methods=['GET', 'POST'])
def add_requirements(project_id, requirement_id):    
    requirement = Requirement.query.get_or_404(requirement_id)
    form = RequirementForm()
    if form.validate_on_submit():
        requirement = Requirement(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(requirement)
        db.session.commit()
        flash('Your requirement has been created!', 'success')
        return redirect(url_for('requirements.list_requirements'))
    return render_template('requirements.html', title='New requirement',
                           form=form, legend='New requirement', requirement=requirement.id, project_id=project.id)

@requirements.route("/projects/<int:project_id>/requirements/<int:requirement_id>/update", methods=['GET', 'POST'])
@login_required
def update_requirement(project_id, requirement_id):
    requirement = Requirement.query.get_or_404(requirement_id)
    form = RequirementForm()
    if form.validate_on_submit():
        requirement.title = form.title.data
        requirement.content = form.content.data
        db.session.commit()
        flash('Your requirement has been updated!', 'success')
        return redirect(url_for('requirements.list_requirements', requirement_id=requirement.id, project_id=project_id))
    elif request.method == 'GET':
        form.title.data = requirement.title
        form.content.data = requirement.content
    return render_template('create_requirement.html', title='Update requirement',
                           form=form, legend='Update requirement')


@requirements.route("/projects/<int:project_id>/requirements/<int:requirement_id>/delete", methods=['POST'])
@login_required
def delete_requirement(project_id, requirement_id):
    requirement = Requirement.query.get(requirement_id)
    db.session.delete(requirement)
    db.session.commit()
    flash('Your requirement has been deleted!', 'success')
    return redirect(url_for('requirements.list_requirements', project_id=project_id))
