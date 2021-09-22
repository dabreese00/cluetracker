# ClueTracker

A service that records Clue Games, including the players and cards involved, and
all known facts about which players hold, or do not hold, or may have shown,
which cards.


## Develop

The frontend is ReactJS.  The backend/API is Django Rest Framework.

Development can be done using docker-compose.  To run it, clone the repository,
then:

1.  Install Docker and `docker-compose`.
2.  `cd` into the repository root.
3.  Adjust the environment variables in the `.env-docker` files and `.env-docker-postgres` if necessary.
4.  Run `docker-compose build`.
5.  Run `docker-compose up`.
6.  Access the API server on `http://localhost:8000/api/games`.
7.  Access the web server on `http://localhost:3000`.

If the API service fails at first because postgres is not available yet, stop
the docker containers (without destroying them) and try again.  (TODO:
Implement a check-and-wait till postgres is up, using e.g.  `django-probes`.)

For now, since self-registration and login is not implemented yet, you need to
create an admin user in the backend in order to allow the frontend to talk to
the API.  Make sure the variables in `frontend/.env-docker` file match
whatever credentials you setup here:

    docker-compose exec api python manage.py createsuperuser

To run tests inside Docker, use the following commands:

    docker-compose exec api python manage.py test [my.tests.module]
    docker-compose exec web npm test

### Auto-reloading with docker-compose and bind mounts

Most of the time while the docker-compose is running, changes to the Django
code should trigger an auto-reload thanks to Gunicorn's `--reload` option.  
Changes to models will naturally require manual action to migrate.  Changes to
`settings.py` may require a container restart.  Changes to `requirements.txt`
require a full rebuild of the container.

Note that due to the bind mounts -- which enable reloading using docker -- the
docker containers WILL edit the contents of the local directories.  In
particular, they'll create and update the `build` and `node_modules`
directories for the React frontend, and the `staticfiles` directory for the
Django backend.  All of these directories are `.gitignore`d.


### Develop with frameworks' local dev servers

Alternately, you can use Django's and React's built-in development servers to
develop.  In this case, adjust the `.env` (non-`-docker`) files appropriately,
and then open two terminal windows.

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
    cd cluetracker
    pip-sync requirements.txt dev-requirements.txt

The second assumes you've already installed [Node](https://nodejs.org/en/) version 16 or higher.  If not, do that first, recommend using [nvm](https://github.com/nvm-sh/nvm).

Then you can run the Django and React (Jest) tests the normal way.
