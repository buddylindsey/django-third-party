#!/usr/bin/env python

from setuptools import setup

setup(
    name='django-third-party',
    version='0.1.0',
    description='Add third party scripts and css to specific paths via db.',
    author='Buddy Lindsey',
    author_email='buddy@buddylindsey.com',
    url='https://github.com/buddylindsey/django-third-party',
    packages=[
        'dj_thirdparty', 'dj_thirdparty.migrations'],
    install_requires=[
        'Django>=1.8', 'six', 'django_extensions'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management'],
)
