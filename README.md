# 316epilepsy
## Explanation of files
The flask app is inside the folder flask_qa.

The following files compose the app's contents:
* models.py - this file creates the features of the tables in the database. When the table structure is updated, the command `flask create_tables` should be run in the vitrual environment (see below).
* routes/main.py - this file creates the endpoints for the app, which represent and render the different pages. 
* static/* - these files includes the CSS, which is developed from the Bootstrap template
* templates/* - these files are the html for the pages. Not all are currently used. 

The following files congigure the app to Flask or Heroku. They should not be edited:
* __init__.py - this file configures the app with Flask
* extensions.py - this file initializes login and sqlalchemy
* settings.py - this file configures the app with Flask
* Pipfile - this file configures the app with Flask and will be auto-updated with new installations
* Pipfile.lock - this file is updated with the Pipfile
* Procfile - this file configures the app for Heroku
* wsgi.py - this file configures the app for Flask

The following files are miscellaneous:
* db.sqlite3 - this file is the database for the app when run on your local machine

## How to run locally
Run the following commands in the git repo folder on your local machine. 
If this is the first time you are running, install flask-login and flask-sqlalchemy:
* `pip install flask-login` and * `pip install flask-sqlalchemy` to install both packages on your machine
If you have run before, you can skip to the following steps: 
* `pipenv install flask` to create a virtual environment.
* `pipenv shell` to enter the virtpipepipenv ual environment.
* `pipenv install` to install everything in the Pipfile into your virtual environment
* `flask run` to run the app locally. 
Visit the given address to access the app.

## How to run on Heroku
Heroku is setup to deploy the app automatically for every push to master in the git repo. On Heroku, click "Open App" or visit https://epilepsycenter.herokuapp.com/ when the build has succeeded and the app has been deployed (in latest activity under "Overview"). If there is an error, view the logs under "More" next to "Open App."

## Loading Production Dataset
Since we do not have a production dataset for reasons listed on the progess report, you cannot upload any data. 