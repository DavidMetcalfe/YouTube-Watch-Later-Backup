import sys
import os
from distutils.core import setup

setup(
    name='browsercookie',
    version='0.7.1',
    packages=['browsercookie'],
    # look for package contents in current directory
    package_dir={'browsercookie': '.'},
    author='Richard Penman',
    author_email='richard@webscraping.com',
    description='Loads cookies from your browser into a cookiejar object so can download with urllib and other libraries the same content you see in the web browser.',
    url='https://bitbucket.org/richardpenman/browsercookie',
    install_requires=['pycryptodome', 'keyring'],
    license='lgpl'
)
