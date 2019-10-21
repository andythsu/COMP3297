#!/bin/bash

printf "path of pip...\n"
which pip
read -p "does it point to the virtual env in current project [y/N] ? " answer

if [ "$answer" == "y" ]; then
  # freezing dependencies before push
  printf "freezing dependencies...\n"
  pip freeze > requirements.txt
fi