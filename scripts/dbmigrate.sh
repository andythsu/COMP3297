#!/bin/bash

appName="wolfpack"

# this will let Django know we have some changes in our model
./manage.py makemigrations $appName

# this will apply changes to database
./manage.py migrate $appName

# sync db
./manage.py migrate --run-syncdb