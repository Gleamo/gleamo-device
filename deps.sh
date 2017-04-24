#!/bin/bash

command -v pip >/dev/null 2>&1 || { echo >&2 "I require pip but it's not installed. See https://bootstrap.pypa.io/get-pip.py. Aborting."; exit 1; }

pip install 'termcolor>=1.1.0'
pip install 'gpio>=0.2.0'
