import unittest

loader = unittest.TestLoader()
tests = loader.discover('.', '*_test.py')
testRunner = unittest.runner.TextTestRunner()
testRunner.run(tests)
