#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import setuptools


author = 'Dave Vandenbout'
email = 'devb@xess.com'
version = '1.1.0'

if 'sdist' in sys.argv[1:]:
    with open('kinparse/pckg_info.py','w') as f:
        for name in ['version','author','email']:
            f.write("{} = '{}'\n".format(name,locals()[name]))

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # Put package requirements here
    'future >= 0.15.0',
    'pyparsing >= 2.1.1',
]

test_requirements = [
    # Put package test requirements here
    'pytest',
]

setup(
    name='kinparse',
    version = version,
    description="Parser for KiCad schematic netlists.",
    long_description=readme + '\n\n' + history,
    author = author,
    author_email= email,
    url='https://github.com/devbisme/kinparse',
    project_urls={
        "Documentation": "https://devbisme.github.io/kinparse",
        "Source": "https://github.com/devbisme/kinparse",
        "Changelog": "https://github.com/devbisme/kinparse/blob/master/HISTORY.rst",
        "Tracker": "https://github.com/devbisme/kinparse/issues",
    },
#    packages=['kinparse',],
    packages=setuptools.find_packages(exclude=['tests']),
    entry_points={'console_scripts':['kinparse = kinparse.__main__:main']},
    package_dir={'kinparse':
                 'kinparse'},
    include_package_data=True,
    package_data={'kinparse': ['*.gif', '*.png']},
    scripts=[],
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='kinparse KiCad netlist parsing',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
    ],
    test_suite='tests',
    tests_require=test_requirements
)
