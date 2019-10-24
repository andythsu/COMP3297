#!/bin/bash

echo "installing virtualenv using pip..."
pip install virtualenv

virtualEnvName="venv"

echo "creatng virtual env named $virtualEnvName..."
virtualenv $virtualEnvName

echo "activating current virtual env..."
source $virtualEnvName/Scripts/activate

# install dependencies
./install.sh