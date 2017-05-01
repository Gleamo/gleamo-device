#!/bin/bash

# check python is installed
if [[ $(python --version 2>&1) != *3\.* ]]; then
  echo "Please install Python 3"
  exit
fi

# check pip is installed
if [[ $(pip --version 2>&1) != *9\.* ]]; then
  echo "Please install pip >9.0.0"
  exit
fi

command -v pip >/dev/null 2>&1 || { echo >&2 "I require pip but it's not installed. See https://bootstrap.pypa.io/get-pip.py. Aborting."; exit 1; }

# install dependencies
pip install 'termcolor>=1.1.0'
pip install 'gpio>=0.2.0'
