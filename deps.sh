#!/bin/bash

# check python is installed
if [[ $(python3 --version 2>&1) != *3\.* ]]; then
  echo "Please install Python 3"
  exit
fi

# check pip is installed
command -v pip3 >/dev/null 2>&1 || { echo >&2 "I require pip but it's not installed. See https://bootstrap.pypa.io/get-pip.py. Aborting."; exit 1; }

# install dependencies
pip3 install 'termcolor>=1.1.0'
pip3 install 'gpio>=0.2.0'
pip3 install 'pika>=0.10.0'
