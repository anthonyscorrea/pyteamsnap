from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Python package to interface with TeamSnap API'
LONG_DESCRIPTION = 'https://www.teamsnap.com/documentation'

# Setting up
setup(
    name="teamsnap-python",
    version=VERSION,
    author="Anthony Correa",
    author_email="a@correa.co",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "api-client",
        "collection_json"
    ],

    keywords=['teamsnap'],
    classifiers=[
    ]
)