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
if on windows 10 PowerShell
create and run virtualenv
```
pip install virtualenv
virtualenv [env name]
cd [env name]/Scripts
cmd
activate.bat
```
If on UNIX
```
pip install virtualenv
virtualenv [env name]
source [env name]/bin/activate

```
open requirements.txt to ensure libraries are installed, run
```
pip install [libraries in requirements file]

```

Environment Variables required (default using smtp.google 587)
```
EMAIL_USERNAME
EMAIL_PASS
SQLALCHEMY_DATABASE_URI
SECRET_KEY
REDIS_URL
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
otherwise use for test and production servers
```
gunicorn application:application
```

*Note: you may need to initialize the db, please refer to http://flask-sqlalchemy.pocoo.org/2.3/quickstart/ for more information
