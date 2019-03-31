from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import timedelta
import redis
myredis = redis.Redis(host='localhost',port=6379,db=0)

application = Flask(__name__)
# Secret key required always
application.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7)
application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# Local Database
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# AWS RDS Database
# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(user='admin', password='#Y_)~-s]LB2t', server='projectmanagementservicetest.cjkwv9ccpled.us-east-1.rds.amazonaws.com:3306', database='projectdb')
# application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{server}/{database}'.format(user='admin', password='projecttesting1', server='projectmanagementservice.cjkwv9ccpled.us-east-1.rds.amazonaws.com:3306', database='projectdb')
application.debug = True


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
