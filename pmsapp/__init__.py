from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

application = Flask(__name__)
# Secret key required always
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# Local Database
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# AWS RDS Database
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(user='admin', password='#Y_)~-s]LB2t', server='projectmanagementservicetest.cjkwv9ccpled.us-east-1.rds.amazonaws.com:3306', database='projectdb')

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
migrate = Migrate(application, db)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
#create all db tables
@application.before_first_request
def create_tables():
    from pmsapp import models
    db.create_all()


from pmsapp import routes
