# studentform


Description
  This is a CRUD base for Python/Django. It relies only in HTML forms and submits to persist data.

Installation 
> Create a folder named student 
> create a virtual enviroment called myvenv
> activate that enviroment
> pip install mysql django

Creating new project
>creating new project name studentproject(django-admin startproject studentproject)
>creating new app nae studentapp(django-admin startapp studentapp)



Configure the app
 In settings.py
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER':'root',
        'PASSWORD':'',
        'PORT':'3306',
        'HOST':'localhost',
    }
}
in name enter database name
in password enter your mysql pasword

INSTALLED_APPS = [
    
    'studentapp',
]

Then create a database in mysql by using mysql query(create database databasename;)

to finish configuration

> python manage.py sql migrate
> python manage.py makemigrations
>python manage.py migrate

add the records into models.py 
after that views.py
In studentapp create a templates folder inside that create index.html and read.html
pass the url into urls.py

Finally to run the server 

>py manage.py runserver
>navigate  to the app adress







