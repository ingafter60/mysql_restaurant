# Building Restaurant Site Using Django 2.1.4 and MySQL

## Section 2 - Create Our Restaurant Project

## 2. Creating the Restaurant Project

1. Create Django Project

	> django-admin startproject mysql_restaurant

2. Create the database

  > CREATE DATABASE django_mysql_restaurant;
  > CREATE USER 'restaurant'@'localhost' IDENTIFIED BY 'restaurant';
  > GRANT ALL PRIVILEGES ON django_mysql_restaurant.* TO 'restaurant'@'localhost';
  > FLUSH PRIVILEGES;

  > show grants for 'restaurant'@'localhost';                             
	+---------------------------------------------------------------------------+
	| Grants for restaurant@localhost                                           |
	+---------------------------------------------------------------------------+
	| GRANT USAGE ON *.* TO `restaurant`@`localhost`                            |
	| GRANT ALL PRIVILEGES ON `django_restaurant`.* TO `restaurant`@`localhost` |
	+---------------------------------------------------------------------------+

3. Setting the database credentials

	DATABASES = {
    'default': {
        'ENGINE'	: 'django.db.backends.mysql',
        'NAME'		: 'django_mysql_restaurant',
        'USER'		: 'restaurant',
        'PASSWORD': 'restaurant',
        'HOST'		: 'localhost',
        'PORT'		: '3306',
    }
	}		

4. Run the server

	> python manage.py runserver
	...
	django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module.
	Did you install mysqlclient?

5. Modify __init__.py file by adding this

	import pymysql
	pymysql.install_as_MySQLdb()

5. Re Run the server

	> python manage.py runserver
	...
	raise RuntimeError("cryptography is required for sha256_password or caching_sha2_password")
	RuntimeError: cryptography is required for sha256_password or caching_sha2_password

6. Install cryptography

	> pip install cryptography

7. Re Run the server

	> python manage.py runserver
	...
	Starting development server at http://127.0.0.1:8000/

8. Create user table

	> python manage.py migrate

9. Create superuser

	> python manage.py createsuperuser

## 3. Creating Our Meals App

	> python manage.py startapp meals

	> create Meals model

	> register Meals model to admin.py

	> create human readabe word using class Meta

	> displaying name as name, NOT as an object in admin panel

## 4. Adding Slug in Meals

	> import slugify to the model

	> add slug to the Meals model

	> add slug def to the model

## 5. Setup Static & Media

	> Add static media root dir to settings
	> Import settings, static file to project's url

## 6. Adding Meals List View

	> include the meals's url to project url

	> define urlpatterns in meals's url

	> create template/Meals/list.html in meals

	> def in views to display the list.html

## 7. Adding Meals Detail View

	> in views add mail_detail

	> in url add the path using slug

	> create detail.html in Template/Meals

	> display the detail meal

## 8. Adding Templates Part 1

	> add static files

	> add template and base html

	> add list html (ex index.html)

	> load static files

	> use block to use base.html and list.html

	> load css and js

## 9. Adding Templates Part 2

	> add detail.html page

	> display meal detail

## 10. Adding Category Models

	> create Category model

	> add Category as FK in Meals model
	
	> create class Meta

	> create human readable Category

	> add category to views as part of meal_list


## 12. Adding Reserve Table model

	> create reservation app

	> add to reservation: templates/Reservation/reservation.html

	> register the new app

	> create Reservation model

	> register reservation in admin

	> migrations and migrate + check the result in admin + test it out

	> add to views

	> create a new urls.py + app_name = 'reservation' 

	> add route path in main urls.py
