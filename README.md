## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate
    $ python manage.py createsuperuser

2) Run Django

    $ python manage.py runserver $IP:$PORT

3) Deploying Python and Django Apps on Heroku

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip freeze > requirements.txt

4) Procfile

    $ web: gunicorn gettingstarted.wsgi --log-file -

5) Database configuration

    $ sudo easy_install psycopg2
    $ sudo easy_install dj-database-url
import dj_database_url

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

6) Serving static files in production

    $ 
