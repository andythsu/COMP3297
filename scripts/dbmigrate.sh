#!/bin/bash

# this will let Django know we have some changes in our model
./manage.py makemigrations

# this will apply changes to database
./manage.py migrate