# API web services with Django REST Framework v1.0.0

A web API REST for services and schedules using [MVC Django framework](https://www.djangoproject.com/) and [Django REST Framework.](https://www.django-rest-framework.org/)

This README would normally document whatever steps are necessary to get the
application up and running.

Things you may want to cover:

## Python version

python 3.7.0

## System dependencies

Please review the [requirements file](requirements.txt) for details.

## Configuration

This application runs on development environment from a localhost server and port 8000

Database server configuration is defined for SQLite3, for modifying parameters and details check [database configuration file](webapp/settings.py)

## Database creation and initialization

Check if you are on project root directory and run on your console or CLI next command:

* python manage.py migrate

## Deployment instructions

Before database creation and initialization, check if you are on project root directory and run on your console or CLI next command for installing dependencies:

* python -m pip install django
* python -m pip install djangorestframework
* python -m pip install django-extensions

After database creation and initialization, check if you are on project root directory and run on your console or CLI next commands for checking dependencies and running server:

* python -m pip freeze
* python manage.py runserver

Check on your console or CLI if your localhost server is running, after that, type [localhost:8000](http://localhost:8000) on your browser and check if you can view home page.

If you want to login Django admin panel and manage API data, you must run first on your console or CLI next command for creating a superuser:

* python3 manage.py createsuperuser

after type (http://localhost:8000/admin/) on your browser and fill form with your username and password provided before.

## Routing dependencies

Please check [URLs project configuration file](gradiweb/urls.py) and [URLs webapp configuration file](webapp/urls.py)

You can view all routes, running on your console or CLI next command from project root directory:

* python manage.py show_urls

## Next improvements and changes

* Deployment on any cloud environment
