# ClueTracker

A service that records Clue Games, including the players and cards involved, and
all known facts about which players hold, or do not hold, or may have shown,
which cards.

## Develop

Development can be done using docker-compose with gunicorn and postgres,
instead of the built-in Django development server.

To run it:

1.  Install Docker and `docker-compose`.
2.  Pass the environment variables to docker using `.env-docker` and `.env-docker-postgres`.
    1. Required variables for Django: `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, `DATABASE_URL`.
    2. Required variables for postgres: `POSTGRES_USER`, `POSTGRES_PASSWORD`.
3.  Run `docker-compose build`.
4.  Run `docker-compose up`.
5.  Access the server on `localhost:8000`.

For development you can set the `DJANGO_ALLOWED_HOSTS` to be `*`.

If the web service fails to start at first because postgres is not available
yet, stop the docker containers (without destroying them) and try again.
(TODO: Implement a check-and-wait till postgres is up, using e.g.
`django-probes`.)

To run tests in docker, after the docker-compose is up and running, use the
following command:

    docker-compose exec web cluetracker/manage.py test

Append whatever test modules you want to run to the end of the argument list.

You can alternatively run tests locally, if you've got Python and a virtual env:

    cluetracker/manage.py test

When doing so, don't forget to `migrate` first (the Docker method automates
this).

As for `makemigrations`, it can be run either using Docker or locally.

Most of the time while the docker-compose is running, changes to the code
should trigger an auto-reload thanks to Gunicorn's `--reload` option, but
changes to models will require manual action to migrate, and changes to the
requirements.txt will require a full rebuild of the container.
