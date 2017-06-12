#!/usr/bin/env python

import os
import sys
from setuptools import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload --sign')
    os.system('python setup.py bdist_wheel upload --sign')
    sys.exit()


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')


setup(name = "dj-stripe", version = "1.0.0", long_description=readme + '\n\n' + history)
