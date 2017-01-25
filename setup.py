#!/usr/bin/env
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from os import path

def read(name):
    return open(path.join(path.dirname(__file__), name)).read()

setup(
    name='django-facebook-auth-manager',
    version='0.1.0',
    description="Django implementation for Facebook authentication.",
    long_description=read("README.rst"),
    url="https://github.com/pinetree408/django-facebook-auth",
    maintainer="Sangyoon Lee",
    maintainer_email="pinetree408@gmail.com",
    author='Sangyoon Lee',
    author_email='pinetree408@gmail.com',
    license='MIT License',

    install_requires=(
        'Django',
    ),

    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],

    packages=[
        'django_facebook_auth',
    ],
)
