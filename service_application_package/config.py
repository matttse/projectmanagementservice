import os
from datetime import timedelta

class Config:
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY='5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:projecttesting1@projectmanagementservice.cjkwv9ccpled.us-east-1.rds.amazonaws.com:3306/projectdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
