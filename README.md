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

4) Run Django

    $ python manage.py runserver $IP:$PORT
