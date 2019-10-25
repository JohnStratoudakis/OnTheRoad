# OnTheRoad

[![Build Status](https://travis-ci.org/JohnStratoudakis/OnTheRoad.svg?branch=master)](https://travis-ci.org/JohnStratoudakis/OnTheRoad) [![PyPI version](https://badge.fury.io/py/OnTheRoad.svg)](https://badge.fury.io/py/OnTheRoad)

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
