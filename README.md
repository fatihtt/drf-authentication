# drf_auth

## Example and source code for django rest framework token authentication


* Install project
> `py -m django startproject [project_name]`

* Install and activate virtual environment
> `python -m venv .venv`

> `.\.venv\Scripts\activate`

* Install django rest framework
>`pip install django djangorestframework`

* Create requirements.txt
> `pip freeze > requirements.txt`

* Create api within project
> `python manage.py startapp api`

* Add djangorestframework and api to the installed apps on settings of project

* Add json web token plugin to api
> `pip install djangorestframework-simplejwt`

#### * If there is an import problem on VSCode:
> Ctrl + Shift + P -> Type and select 'Python: Select Interpreter' and select virtual environment
