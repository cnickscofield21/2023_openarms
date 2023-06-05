# Setting Up Python-Django Environment

This project was developed using:

* Python 3.10.6

* Django 4.2.2

* Postgres 14.7

* psycopg2_binary 2.9.6

## Unix Installation Commands

Install python using instructions found at [python.org](https://www.python.org/downloads/)

Install and setup Django as follows:

1. Install virtual environment:

> $ ``python3 -m pip install --user virtualenv``

2. Create working directory:

> $ ``mkdir 2023_openarms``

3. Enter working directory, create virtual environment:

> $ ``python3 -m venv venv``

4. Activate virtual environment:

> $ ``source venv/bin/activate``

5. Create requirements file:
> $ ``touch requirements.txt``

6. Add Django to the list of requirements by adding the folling to requirements.txt:

> Django==4.2.2

7. Install Django:

> $ ``pip install -r requirements.txt``

8. Create project:

> $ ``django-admin startproject OpenArmsRoot .``

9. Run migrations:

> $ ``python manage.py migrate``

10. Start server:

> $ ``python manage.py runserver``

11. View server [output](http://localhost:8000)

12. Download & install [PostgreSQL](https://www.postgresql.org/download/)

13. Add Django to the list of requirements by adding the folling to requirements.txt:

> psycopg2_binary==2.9.6

14. Install a PostgreSQL adapter for Python:

> $ ``pip install psycopg2-binary``

15. Create database and user:

> $ ``sudo su postgres``

> $ ``psql``

> postgres=# ``CREATE DATABASE openarmsdb;``

> postgres=# ``CREATE USER openarms WITH PASSWORD '<SOME STRING HERE>';``

> postgres=# ``GRANT ALL PRIVILEGES ON DATABASE openarmsdb TO openarms;``

> postgres=# ``ALTER USER openarms CREATEDB;``

16. Configure DATABASES section of OpenArmsRoot/settings.py file per info file stored offline

17. Re-run migrations to connect to PostgreSQL rather than initial SQLite DB

> $ ``python manage.py migrate``

18. From root of project run:

> $ ``django-admin startapp OpenArmsApp``

19. Inside new directory (OpenArmsApp), delete all new files EXCEPT:

> \_\_init\_\_.py

> apps.py

20. Open OpenArmsApp/apps.py, edit the file so it reads as follows:

> from django.apps import AppConfig
>
>
> class OpenarmsConfig(AppConfig):
>     default_auto_field = 'django.db.models.BigAutoField'
>     name = 'OpenArmsApp'
>     label = 'OpenArmsApp'

21. Open OpenArmsRoot/settings.py, edit the file so it reads as follows:

> \# Application definition
>
> INSTALLED_APPS = [
>
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
>     'OpenArmsApp'
> ]

23. Create User model. From project root:

> $ ``cd OpenArmsApp && django-admin startapp user``

---

## Windows Installation Commands

Install python using instructions found at [python.org](https://www.python.org/downloads/)

Install and setup Django as follows:

1. Install virtual environment. Run:

> $ ``py -m pip install --user virtualenv``

2. Create working directory:

> $ ``mkdir 2023_openarms``

3. Enter working directory, create virtual environment:

> $ ``py -m venv venv``

4. Activate virtual environment:

> $ ``./venv/Scripts/activate``

5. Create requirements file:

> $ ``cd > requirements.txt``

6. Add Django to the list of requirements by adding the folling to requirements.txt:

> Django==4.2.1

7. Install Django:

> $ ``pip install -r requirements.txt``

8. Create project:

> $ ``django-admin startproject OpenArms .``

9. Run migrations:

> $ ``python manage.py migrate``

10. Start server:

> $ ``python manage.py runserver``

11. View server [output](http://localhost:8000)

12. Download & install [PostgreSQL](https://www.postgresql.org/download/)

13. Add Django to the list of requirements by adding the folling to requirements.txt:

> psycopg2_binary==2.9.6

14. Install a PostgreSQL adapter for Python:

> $ ``pip install psycopg2-binary``

15. Create database and user: <b style="color:red;">WINDOWS STEPS NOT LISTED IN SOURCE MATERIAL</b>

16. Configure DATABASES section of settings.py file per info file stored offline

17. Re-run migrations to connect to PostgreSQL rather than initial SQLite DB

> $ ``python manage.py migrate``

18. From root of project run:

> $ ``django-admin startapp OpenArmsApp``

19. Inside new directory (OpenArmsApp), delete all new files EXCEPT:

> \_\_init\_\_.py

> apps.py

20. Open OpenArmsApp/apps.py, edit the file so it reads as follows:

> from django.apps import AppConfig
>
>
> class OpenarmsConfig(AppConfig):
>     default_auto_field = 'django.db.models.BigAutoField'
>     name = 'OpenArmsApp'
>     label = 'OpenArmsApp'

21. Open OpenArmsRoot/settings.py, edit the file so it reads as follows:

> \# Application definition
>
> INSTALLED_APPS = [
>
>     'django.contrib.admin',
>     'django.contrib.auth',
>     'django.contrib.contenttypes',
>     'django.contrib.sessions',
>     'django.contrib.messages',
>     'django.contrib.staticfiles',
>     'OpenArmsApp'
> ]