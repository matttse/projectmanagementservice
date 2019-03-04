from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate

application = Flask(__name__)
# UNCOMMENT THIS TO RUN LOCALDB for development
# application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# AWS config from object
# application.config.from_object('config')
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{password}@{server}:{port}/{database}'.format(user='admin', password='#Y_)~-s]LB2t', server='projectmanagementservicetest.cjkwv9ccpled.us-east-1.rds.amazonaws.com', port='3306', database='projectdb')

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
migrate = Migrate(application, db)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

if __name__ == '__main__':
    application.run(debug=True)
