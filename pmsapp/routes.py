from flask import render_template, url_for, flash, redirect, request
from pmsapp import app, db, bcrypt
from pmsapp.forms import RegistrationForm, LoginForm
from pmsapp.models import User, Project
from flask_login import login_user, current_user, logout_user, login_required


project = [
    {
        'author': 'Test Name Autho',
        'title': 'Project',
        'content': 'First post content',
        'date_posted': 'blah blah date'
    },
    {
        'author': 'Author 2',
        'title': 'Project 2',
        'content': 'Second post content',
        'date_posted': 'todo date'
    }
]


@app.route("/")
def home():
    return render_template('home.html', title=home)

@app.route("/projects")
def projects():
    return render_template('projects.html', project=project)


@app.route("/issues")
def issues():
    return render_template('issues.html', title='Issues')

@app.route("/chat")
def chat():
    return render_template('chat.html', title='Chat')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('projects'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('projects'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('projects'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('projects'))


@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')
