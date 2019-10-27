# OnTheRoad

[![Build Status](https://travis-ci.org/JohnStratoudakis/OnTheRoad.svg?branch=master)](https://travis-ci.org/JohnStratoudakis/OnTheRoad) [![PyPI version](https://badge.fury.io/py/OnTheRoad.svg)](https://badge.fury.io/py/OnTheRoad)

Are you planning a road trip or a train trip and want to figure out what path to take while visiting the most cities in your path?

This is a Python Flask app with a React JS front end that uses the mlrose Traveling Salesperson Library to calculate an optimal path through multiple cities, without having to return to the original city.

I did this because I live in New York City and like to do Euro Trips where I fly in through let's say Amsterdam and I fly out from London.  (I actually did this back in May of 2019 where I flew to Amsterdam, spend 3 days there then took the train to Brussels, spent the night and then took the train to London, spent three days there and flew back to New York City via London)

# Fedora Core 27
I had to install pip3.7 by running:

```wget https://bootstrap.pypa.io/get-pip.py```

# How I set up continuous delivery to pypi from Travis-CI

## and then installing it via:

```sudo python3.7 ./get-pip.py```

## I created a .pypirc-bot file
```[distutils]
index-servers=pypi testpypi

[pypi]
repository_url: https://test.pypi.org/legacy
username: <my-username>
password: <my-password>

[testpypi]
repository_url: https://test.pypi.org/legacy
username: <my-username>
password: <my-password>
```

## I created a public-private key pair
```ssh-keygen -f travis_deploy_key```

## I created a tar
```tar cvf secret-files.tar .pypirc-bot travis_deploy_key```

## I logged in to travis
```travis login --org```

## I encrypt the tar file
```travis encrypt-file -r JohnStratoudakis/OnTheRoad secret-files.tar --add```

## I add the encrypted tar file to git
 ```git add secret-files.tar.enc```

## commit and push
git commit -m "Adding deploy key and pypirc file for continuous delivery"

## This repo helped me figure out how to use bumpversion properly:
https://github.com/guettli/github-travis-bumpversion-pypi
