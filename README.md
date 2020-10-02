# Hired Django RESTful App

This is the back-end counterpart to the full-stack [Datr Prototype](https://github.com/kurtkrafft1/dater-prototype). A full description of the app can be found there.

# Project Setup

1.  Please Note that you must place the following steps in a separate directory from the front end app!!!!

1.  Clone the repo and cd into the `d8r-api` directory you made after setting up the react app:

    `git clone git@github.com:kurtkrafft1/dater_prototype_api.git`

1.  Navigate to the root directory:
    `cd dater_prototype_api`

1.  Set up your virtual environment:

    `python -m venv daterEnv`

1.  Activate virtual environment:

    `source ./daterEnv/bin/activate`

1.  Install dependencies:

    `pip install -r requirements.txt`

1) In the terminal now we can run migrations:

   `python manage.py makemigrations`
   `python manage.py migrate`

1) Now we need to make migrations for the app itself and the models within it

   `python manage.py makemigrations daterapp`
   `python manage.py migrate`

1) in your terminal it is time to load fixtures:

   `python manage.py loaddata */fixtures/*.json`

1. Start the API server:

   `python manage.py runserver`

1. Follow the [steps on the front-end web app readme](https://github.com/kurtkrafft1/Hired) to view the web app in your browser

## Technology Utilized

1. Django
1. Python
1. SQLite
1. Fixtures
1. ORM & SQL queries
1. Models
1. API Endpoint Views

## Made By:

- [Kurt Krafft](https://github.com/kurtkrafft1)
