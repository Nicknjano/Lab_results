## Features:
 - The polls application is extended to a survey where admin can create multiple surveys with multiple questions and choices for each question.
 - The dashboard is enriched with a statistics widget. The widget displays the popular survey among the surveys and the bar chart visualization of vote distributions among different choices for a question.
 - The application is a SPA with 5 Views on the Users App and a dashboard for the administrator. Partial Views are implemented with a custom middleware view 'index' which further routes URL requests.
 - Created two REST endpoints and used them from admin through AJAX calls.
 
## Installation and Launching the application

### Requirements:

- python version > 3.6 installed
- django version > 3.1.5 installed
```cmd
python -m pip install django
```
- nested-admin > 3.3.3 installed
```cmd
pip install django-nested-admin 
```
or
```cmd
python -m pip install django-nested-admin 
```
### Run
#### Check for possible schema changes while using the version control as well as for the first run. 
Navigate to the project directory (where manage.py is located) and run
  ```cmd
  python manage.py makemigrations survey
  ```
#### Create schema for models incorporated in survey app. (The sql script returned can be used shared across teams)
  ```cmd
  python manage.py sqlmigrate survey 0001
  ```
#### Commit  all changes to the databases. This also creates necessary tables in the database.
  ```cmd
  python manage.py migrate
  ```
#### Collect all static assets and add to build/root folder in main application scope
  ```cmd
  python manage.py collectstatic
  ```
#### Create an admin user for the application
  ```cmd
  python manage.py createsuperuser
  ```
#### Run the development server
  ```cmd
  python manage.py runserver
  ```
  
 



