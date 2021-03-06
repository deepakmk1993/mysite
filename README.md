# Deploying Python and Django Apps on Heroku
ALLOWED_HOSTS = ['<your app URL without the https:// prefix>.herokuapp.com','127.0.0.1']

1) Run below command to sync models to database and create Django's default superuser and auth system and Run Django

    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver $IP:$PORT

2) Create Virtualenv

    $ virtualenv venv
    $ source venv/bin/activate
    $ pip freeze > requirements.txt

3) Procfile

    $ web: gunicorn gettingstarted.wsgi --log-file -

4) Database configuration

    Install "psycopg" & "dj-database-url" with the following commands:
    $ sudo easy_install psycopg2
    $ sudo easy_install dj-database-url
    settings.py
        import dj_database_url
        db_from_env = dj_database_url.config(conn_max_age=500)
        DATABASES['default'].update(db_from_env)
    OR
        import dj_database_url
        DATABASES['default'] =  dj_database_url.config()

5) WhiteNoise

    $ pip install whitenoise
    $ pip freeze > requirements.txt
    
    wsgi.py
        from django.core.wsgi import get_wsgi_application
        from whitenoise.django import DjangoWhiteNoise
        
        application = get_wsgi_application()
        application = DjangoWhiteNoise(application)

6) Serving static files in production

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
    mkdir static
    Run below command if folder is empty because if your folder is empty then git doesn't commit them
    touch static/.dir
    $ python manage.py collectstatic --noinput


7) Requirements

    $ pip freeze > requirements.txt
        Django==1.9
        dj-database-url==0.4.2
        gunicorn==19.6.0
        psycopg2==2.6.2
        whitenoise==3.2.3

## How To Use PostgreSQL with your Django Application

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
    
    PostgreSQL DB Configuraton
    --------------------------
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'DATABASE_Name',
            'USER': 'myprojectuser',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '',
        }
    }
    SQLite DB Configuraton
    ----------------------
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }


[Django Tutorial Part 11: Deploying Django to production](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)

[Deploying Python and Django Apps on Heroku](https://devcenter.heroku.com/articles/deploying-python)

[Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)

    if bool( os.environ.get('DJANGO_DEBUG', True) )
    	pass
    heroku config:set DJANGO_DEBUG=''
