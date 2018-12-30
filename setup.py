#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import setuptools


author = 'XESS Corp.'
email = 'info@xess.com'
version = '0.0.5'

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
    'pyparsing < 2.3.0',
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
    url='https://github.com/xesscorp/kinparse',
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
    keywords='kinparse',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
