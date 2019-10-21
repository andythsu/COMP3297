#!/bin/bash

echo "installing virtualenv using pip..."
pip install virtualenv

virtualEnvName="venv"

echo "creatng virtual env named $virtualEnvName..."
virtualenv venv

echo "activating current virtual env..."
source $virtualEnvName/Scripts/activate

requirementFile="requirements.txt"

if [ -f "$requirementFile" ]; then
  echo "installing dependencies from requirements.txt..."
  pip install -r requirements.txt
fi