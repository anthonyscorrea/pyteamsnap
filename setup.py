#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['api-client', 'typing-extensions']

test_requirements = [ ]

setup(
    author="Anthony Correa",
    author_email='a@correa.co',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta'
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="An unoffical wrapper for the TeamSnap API",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='pyteamsnap',
    name='pyteamsnap',
    packages=find_packages(include=['pyteamsnap', 'pyteamsnap.*']),
    test_suite='unittests',
    tests_require=test_requirements,
    url='https://github.com/anthonyscorrea/pyteamsnap',
    version='0.2.0',
    zip_safe=False,
)
