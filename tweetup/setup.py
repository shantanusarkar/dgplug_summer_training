#!/usr/bin/env python

"""Shell Dummy project"""

from setuptools import find_packages, setup

dependencies = ['setuptools', 'requests', 'cmd2',]

setup(name = 'facebpost',
    version = '0.3',
    description = "A python script to post facebook status via shell",
    platforms = ["Linux"],
    author = "Shantanu Sarkar",
    author_email = "shantanusarkar.me@gmail.com",
    url = "http://dgplug.org/summertraining/2013/",
    license = "MIT",
    install_requires=[
        "setuptools",
        "requests",
        "cmd2",
        "pyparsing",
    ],
    include_package_data=True,
    scripts = ['facebpost'],
    dependency_links=[
        "https://pypi.python.org/packages/source/r/requests/requests-1.2.3.tar.gz",
        "https://pypi.python.org/pypi/cmd2/0.6.5.1#downloads",
        "https://pypi.python.org/pypi/pyparsing/1.5.7#downloads",
    ],
    packages = find_packages()
    )
   
