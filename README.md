# A solution for the Peaks Test

This repository hosts a solution for the Peaks test for MFI.

## Features

The chosen solution lies with Django and Django REST Framework over a PostGIS database for efficient geospatial data querying.

## Getting the Source Code

Clone the repository using SSH

`git@github.com:nux17/mfi.git`

or HTTPS

`https://github.com/nux17/mfi.git`

## Setting up the environment

The Django service and database are running inside Docker containers, get the latest version of Docker [here](https://www.docker.com/products) (developed using Docker version 19.03.5).

### Start containers

To build then start the containers, run `docker-compose up` (`docker-compose up -d` to daemonize the processes).

### Initialize database

To apply database migrations, run `docker-compose run web ./manage.py migrate`

## Accessing the service

Browse to [http://localhost:8000/](http://localhost:8000/) to access the browsable API.

## Tests

To run the tests, run `docker-compose run web ./manage.py tests`, 1 test for boundaries feature should come up with a success.


