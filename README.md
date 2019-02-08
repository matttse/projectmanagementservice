# Project Management Service

A Python Flask MySQL local application

- [Python](https://www.python.org/downloads/) 
- [Flask](http://flask.pocoo.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

run to ensure libraries are installed
```
pip install flask_login
pip install flask_bcrypt
pip install flask_caching
pip install flask_debugtoolbar
pip install flask_migrate
pip install flask_webpack
pip install flask_wtf
```

bootstrap the environment
```
git clone https://github.com/matttse/projectmanagementservice
cd projectmanagementservice
{%- if cookiecutter.use_pipenv == "yes" %}
pipenv install --dev
{%- else %}
pip install -r requirements/dev.txt
{%- endif %}
cp .env.example .env
npm install
npm start  # run the webpack dev server and flask server using concurrently
```

instantiate DBMS
```
flask db init
flask db migrate
flask db upgrade
npm start
```

deploying to production on server
```
export FLASK_ENV=production
export FLASK_DEBUG=0
export DATABASE_URL="<YOUR DATABASE URL>"
npm run build   # build assets with webpack
flask run       # start the flask server
```
