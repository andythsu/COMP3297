#!/bin/bash

requirementFile="requirements.txt"

if [ -f "$requirementFile" ]; then
  echo "installing dependencies from requirements.txt..."
  pip install -r requirements.txt
fi