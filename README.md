# ClueTracker

A service that records Clue Games, including the players and cards involved, and
all known facts about which players hold, or do not hold, or may have shown,
which cards.

## Develop

Development can be done using docker-compose.  To run it:

1.  Install Docker and `docker-compose`.
2.  Adjust the environment variables in the `.env-docker` files and `.env-docker-postgres` if necessary.
3.  Run `docker-compose build`.
4.  Run `docker-compose up`.
5.  Access the API server on `localhost:8000`.
6.  Access the web server on `localhost:5000`.

If the web service fails to start at first because postgres is not available
yet, stop the docker containers (without destroying them) and try again.
(TODO: Implement a check-and-wait till postgres is up, using e.g.
`django-probes`.)

### Develop with frameworks' local dev servers

Alternately, you can use Django's and React's built-in development servers to develop.  In this case, adjust the `.env` files appropriately, and then open two terminal windows.

In the first, run:

    export DJANGO_READ_DOT_ENV_FILE=True
    cd cluetracker
    python manage.py migrate
    python manage.py runserver

In the second, run:

    cd frontend
    npm install
    npm start

The first assumes you've already setup a Python virtualenv with all the required dependencies installed.  If not, do that first:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip
    pip install pip-tools
    pip-sync requirements.txt dev-requirements.txt

The second assumes you've already installed [Node](https://nodejs.org/en/) version 16 or higher.  If not, do that first, recommend using [nvm](https://github.com/nvm-sh/nvm).


### Develop the web frontend

To do.


### Develop the Django REST API

To run tests in docker, after the docker-compose is up and running, use the
following command:

    docker-compose exec api manage.py test

Append whatever test modules you want to run to the end of the argument list.

You can alternatively run tests locally, if you've got Python and a virtual env:

    cluetracker/manage.py test games.tests.test_models
    cluetracker/manage.py test games.tests.test_api

When doing so, don't forget to `migrate` first (the Docker method automates
this).

As for `makemigrations`, it can be run either using Docker or locally.

Most of the time while the docker-compose is running, changes to the code
should trigger an auto-reload thanks to Gunicorn's `--reload` option, but
changes to models will require manual action to migrate, and changes to the
requirements.txt will require a full rebuild of the container.
