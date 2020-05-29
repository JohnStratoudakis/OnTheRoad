#!/usr/bin/python3.7

from setuptools import setup

setup(
    name="OnTheRoad",
    version="0.0.118",
    author="John Stratoudakis",
    author_email="johnstratoudakis@gmail.com",
    license="",
    packages=["OnTheRoad"],
    entry_points={
        "console_scripts": [
            "onTheRoad=OnTheRoad.__main__:main"
            ]
        },
)

