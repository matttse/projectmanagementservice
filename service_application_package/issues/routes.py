from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from service_application_package import db
from service_application_package.models import Issue
from service_application_package.issues.forms import IssueForm

issues = Blueprint('issues', __name__)

@issues.route("/issues")
def issues():
    return render_template('issues.html', title='Issues')