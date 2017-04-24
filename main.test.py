import argparse
from os import path
import unittest
from termcolor import colored

parser = argparse.ArgumentParser(
    description='Test modules',
)
parser.add_argument(
    '--module',
    dest='module'
)
args = parser.parse_args()

directory = args.module or '.'

print('Running tests in ' + colored('"' + path.abspath(directory) + '"', 'green'))

loader = unittest.TestLoader()
tests = loader.discover(directory, '*_test.py')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
