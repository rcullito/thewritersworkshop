To run locally and ouptut logs to stdout

    $ python manage.py runserver

Install Deps

    $ pip install -r requirements.txt


Db Admin & app Setup

    $ createdb python_getting_started
    $ python manage.py migrate
    $ python manage.py collectstatic

Running a Heroku Process locally

    $ heroku local web


Deploying to Heroku

    $ git push heroku master

Open deployed application

    $ heroku open
