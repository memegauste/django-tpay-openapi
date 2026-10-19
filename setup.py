"""Setup file that prepares the package and installs it."""
# 3rd-party
from setuptools import find_packages
from setuptools import setup

setup(
    packages=find_packages(
        exclude=[
            'testapp',
            'testapp.tests',
        ],
    ),
    install_requires=[
        'requests==2.34.2',
        'django==5.2.18',
        'django-money==3.6.2',
    ],
)
