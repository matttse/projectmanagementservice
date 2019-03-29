# Project Management Service

A Python Flask SQLAlchemy application

- [Python](https://www.python.org/downloads/) Only works in 3.6+
- [Flask](http://flask.pocoo.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

clone the environment master environment
```
git clone https://github.com/matttse/projectmanagementservice
cd projectmanagementservice
```

create and run virtualenv on Windows 10 PowerShell
```
pip install virtualenv
virtualenv [env name]
cd [env name]/Scripts
cmd
activate.bat
```

run to ensure libraries are installed
```
pip install flask flask_sqlalchemy flask_bcrypt flask_login flask_mail flask_wtf Pillow pymysql

```

Environment Variables required (default using smtp.google 587)
```
EMAIL_USERNAME
EMAIL_PASS
SQLALCHEMY_DATABASE_URI
SECRET_KEY
```

Static Files
```
Path: /static/
Directory: service_application_package/static/
Path: /static/profile_pics/
Directory: service_application_package/static/profile_pics/
```



deploying to devlopment on server (needs local OS environ vars export/set)
```
python application.py
```

*Note: you may need to initialize the db, please refer to http://flask-sqlalchemy.pocoo.org/2.3/quickstart/ for more information
