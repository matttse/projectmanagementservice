import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_TYPE = 'redis'
    SESSION_REDIS = Redis(host='pmschat.rpwclh.ng.0001.use1.cache.amazonaws.com', port=6379, db=0)
