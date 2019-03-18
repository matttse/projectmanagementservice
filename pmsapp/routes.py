import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from pmsapp import application, db, bcrypt
from pmsapp.forms import RegistrationForm, LoginForm, UpdateAccountForm, ProjectForm, RequirementForm
from pmsapp.models import User, Project, Requirement
from flask_login import login_user, current_user, logout_user, login_required


@application.route("/")
@application.route("/home")
def home():
    return render_template('home.html', title='Home')

@application.route("/issues")
def issues():
    return render_template('issues.html', title='Issues')

@application.route("/chat")
def chat():
    return render_template('chat.html', title='Chat')
# 
# Accounts
# 
@application.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('/'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@application.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@application.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(application.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@application.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)
# 
# Projects
# 

@application.route("/projects/new", methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(project)
        db.session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('list_projects'))
    return render_template('create_project.html', title='New Project',
                           form=form, legend='New Project')


@application.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project.html', title=project.title, project=project)

@application.route("/projects/all")
def list_projects():
    form = ProjectForm()
    projects = Project.query.all()
    return render_template('projects.html', 
                           form=form, title='project', legend="New Project", projects=projects)

@application.route("/projects/<int:project_id>", methods=['GET', 'POST'])
def add_projects(project_id):    
    project = Project.query.get_or_404(project_id)
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(project)
        db.session.commit()
        flash('Your project has been created!', 'success')
        return redirect(url_for('list_projects'))
    return render_template('projects.html', title='New project',
                           form=form, legend='New project', project=project.id)

@application.route("/projects/<int:project_id>/update", methods=['GET', 'POST'])
@login_required
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.author != current_user:
        abort(403)
    form = ProjectForm()
    if form.validate_on_submit():
        project.title = form.title.data
        project.content = form.content.data
        db.session.commit()
        flash('Your project has been updated!', 'success')
        return redirect(url_for('list_projects', project_id=project.id))
    elif request.method == 'GET':
        form.title.data = project.title
        form.content.data = project.content
    return render_template('create_project.html', title='Update Project',
                           form=form, legend='Update Project')


@application.route("/projects/<int:project_id>/delete", methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.author != current_user:
        abort(403)
    db.session.delete(project)
    db.session.commit()
    flash('Your project has been deleted!', 'success')
    return redirect(url_for('list_projects'))

# 
# Requirements
# 
@application.route("/projects/<int:project_id>/requirements/new", methods=['GET', 'POST'])
@login_required
def new_requirement(project_id):
    form = RequirementForm()
    if form.validate_on_submit():
        requirement = Requirement(title=form.title.data, content=form.content.data, project_id=project_id)
        db.session.add(requirement)
        db.session.commit()
        flash('Your requirement has been created!', 'success')
        return redirect(url_for('list_requirements', project_id=project_id))
    return render_template('create_requirement.html', title='New requirement',
                           form=form, legend='New requirement')


@application.route("/projects/<int:project_id>/requirement/<int:requirement_id>")
def requirement(project_id, requirement_id):
    requirement = Requirement.query.get_or_404(requirement_id)
    return render_template('requirements.html', title=requirement.title, requirement=requirement, project_id=project_id)

@application.route("/projects/<int:project_id>/requirements/all")
def list_requirements(project_id):
    form = RequirementForm()
    requirement_count = Requirement.query.filter_by(project_id=project_id).count()
    if requirement_count > 0:
        requirements = Requirement.query.filter_by(project_id=project_id)
    else:
        requirements = 0
    return render_template('requirements.html', 
                           form=form, title='requirement', legend="New requirement", requirements=requirements, project_id=project_id)

@application.route("/projects/<int:project_id>/requirements/<int:requirement_id>", methods=['GET', 'POST'])
def add_requirements(project_id, requirement_id):    
    requirement = Requirement.query.get_or_404(requirement_id)
    form = RequirementForm()
    if form.validate_on_submit():
        requirement = Requirement(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(requirement)
        db.session.commit()
        flash('Your requirement has been created!', 'success')
        return redirect(url_for('list_requirements'))
    return render_template('requirements.html', title='New requirement',
                           form=form, legend='New requirement', requirement=requirement.id, project_id=project.id)

@application.route("/projects/<int:project_id>/requirements/<int:requirement_id>/update", methods=['GET', 'POST'])
@login_required
def update_requirement(project_id, requirement_id):
    requirement = Requirement.query.get_or_404(requirement_id)
    form = RequirementForm()
    if form.validate_on_submit():
        requirement.title = form.title.data
        requirement.content = form.content.data
        db.session.commit()
        flash('Your requirement has been updated!', 'success')
        return redirect(url_for('list_requirements', requirement_id=requirement.id, project_id=project_id))
    elif request.method == 'GET':
        form.title.data = requirement.title
        form.content.data = requirement.content
    return render_template('create_requirement.html', title='Update requirement',
                           form=form, legend='Update requirement')


@application.route("/projects/<int:project_id>/requirements/<int:requirement_id>/delete", methods=['POST'])
@login_required
def delete_requirement(project_id, requirement_id):
    requirement = Requirement.query.filter_by(id=requirement_id).first()
    db.session.delete(requirement)
    db.session.commit()
    flash('Your requirement has been deleted!', 'success')
    return redirect(url_for('list_requirements', project_id=project_id))
