from flask import render_template, request, Blueprint
from service_application_package.models import Project

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    projects = Project.query.order_by(Project.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', projects=projects)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
