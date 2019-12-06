# BackTrack
*BackTrack* is a web-based collaboration tool for Scrum teams. The short-term goals for *BackTrack* are ease the creation, management and tracking of project backlogs - both Product Backlog and Sprint Backlog. Further enhancements will provide management tools for analysis and visualization of project metrics such as velocity and burndown.

## Develop Environment
The develop environment of this project can be installed by executing the *bootstrap.sh* and *install.sh* in */scripts*. That is, run the following command in **bash mode**.
```bash
./scripts/bootstrap.sh # To bootstrap
./scripts/install.sh # To install
```

## Other Useful Scripts
Some useful scripts are built-in for different purposes.
```bash
./scripts/dbflush.sh # To clean up the existing databash
./scripts/dbmigrate # To set up the databash based on the existing models
./scripts/dbsuperuser.sh # To create a superuser for django admin site
./scripts/run.sh # To run server
./scripts/prepush.sh # Before pushing to github repo
```

## Structure of the Project
Although we use Django for developing *BackTrack*, we still try to separate the entire project into **Backend** and **Frontend** to maintain the OO principle. 
### Backend
The backend developers first mainly focus on the implementation of *models.py* for establishing our database model. Then they also to implement some necessary query function in */dao* directory for providing an interface to communicate with the data in database.
### Frontend
The frontend developers first implement some necessary **view** functions in *XXXViews.py* under */wolfpack* directory for transferring the required contents to the templates. Then they also need to implement the *.html* under */wolfpack/templates* for performing the UI of *BackTrack*.

## Usage
### Step 1
Install the develop environment by the steps in **Develop Environment** if needed.
### Step 2
Run the server by 
```bash
./scripts/run.sh # in bash
```
or
```python
python manage.py runserver # in python
```
### Step 3
Create a superuser if needed.
### Step 4
Login to *localhost:8000/admin* (usually *127.0.0.1:8000/admin*) adn create some user records.
### Step 5
Go to the homepage *localhost:8000* (usually *127.0.0.1:8000*) and login to *BackTrack* with the newly created user record.
### Step 6
You are now in *BackTrack* and enjoy your trip.

## Limitations
- Lack of *User Registration*
- Lack of *Analysis Tool* such burndown chart
