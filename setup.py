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
        'requests==2.32.3',
        'django==5.1.2',
        'django-money==3.0.0',
    ],
)
