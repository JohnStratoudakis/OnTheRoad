#!/usr/bin/python3.7

from setuptools import setup

VERSION = "0.0.2"

setup(
    name="Travel",
    version=VERSION,
    author="John Stratoudakis",
    author_email="johnstratoudakis@gmail.com",
    license="",
    packages=["Travel"],
    entry_points={
        "console_scripts": [
            "travel=Travel.travel_main:main"
            ]
        },
)
