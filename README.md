## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run below command to sync models to database and create Django's default superuser and auth system and Run Django

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver $IP:$PORT

2) Run Django

    

# Deploying Python and Django Apps on Heroku
ALLOWED_HOSTS = ['<your app URL without the https:// prefix>.herokuapp.com','127.0.0.1']

3) Create Virtualenv

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip freeze > requirements.txt

4) Procfile

    $ web: gunicorn gettingstarted.wsgi --log-file -

5) Database configuration

    Install "psycopg" & "dj-database-url" with the following commands:
    $ sudo easy_install psycopg2
    $ sudo easy_install dj-database-url
    settings.py
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)

6) Serving static files in production

    $ pip install whitenoise
    $ pip freeze > requirements.txt
    settings.py
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
    STATIC_URL = '/static/'
    
    # Extra places for collectstatic to find static files.
    STATICFILES_DIRS = (
        os.path.join(PROJECT_ROOT, 'static'),
    )
    $ python manage.py collectstatic --noinput

7) WhiteNoise

    $ pip install whitenoise
    $ pip freeze > requirements.txt
    
    wsgi.py
        from django.core.wsgi import get_wsgi_application
        from whitenoise.django import DjangoWhiteNoise
        
        application = get_wsgi_application()
        application = DjangoWhiteNoise(application)

8) Requirements

    $ pip freeze > requirements.txt
        Django==1.9
        dj-database-url==0.4.2
        gunicorn==19.6.0
        psycopg2==2.6.2
        whitenoise==3.2.3

## How To Use PostgreSQL with your Django Application
==================================================
    Start the PostgreSQL service
    ----------------------------
    $ sudo service postgresql start
    -----------------------
    Connect to the service
    -----------------------
    $ sudo su - postgres
    $ psql
    ----------------------------
    Create a PostgreSQL database
    ----------------------------
    Make sure you have logged into the PostgreSQL terminal and then you can just run:
    $ postgres=# CREATE DATABASE "DB_NAME";
    ------------------
    List all databases
    ------------------
    postgres=# \list
    --------------------------------------
    Set a password for your postgres user.
    --------------------------------------
    $ psql
    $ postgres-# \password postgres
    Enter new password: