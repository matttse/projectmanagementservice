from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from service_application_package.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(Config)

    db.init_app(application)
    bcrypt.init_app(application)
    login_manager.init_app(application)
    mail.init_app(application)

    from service_application_package.users.routes import users
    from service_application_package.projects.routes import projects
    from service_application_package.requirements.routes import requirements
    from service_application_package.stories.routes import stories
    from service_application_package.issues.routes import issues
    from service_application_package.main.routes import main
    from service_application_package.chat.routes import chatroombp
    from service_application_package.errors.handlers import errors
    application.register_blueprint(users)
    application.register_blueprint(projects)
    application.register_blueprint(requirements)
    application.register_blueprint(stories)
    application.register_blueprint(issues)
    application.register_blueprint(main)
    application.register_blueprint(chatroombp)
    application.register_blueprint(errors)

    return application
