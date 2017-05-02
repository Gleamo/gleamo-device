#!/bin/bash

# XXX
# http://hackthology.com/how-to-write-self-updating-python-programs-using-pip-and-git.html
pip3 install --upgrade --src="$HOME/.src" -e git+<URL>@<REV>#egg=PACKAGE_NAME
