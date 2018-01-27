# gifz-api

> Create super user with username admin, he will be author of
> populate_db_from_dir gifs.

> ```
> docker-compose -f dev.yml run --rm django python manage.py migrate
> docker-compose -f dev.yml run --rm django python manage.py createsuperuser
> docker-compose -f dev.yml run --rm django python manage.py populate_db_from_dir ./gifs_db/
> ```

TODO

* flake8 - always multiple statements in arguments, list, tuples, dicts
* flake8 - always oneline before class declaration

* docker user, better dockerfile
* DDD zrobić z tego
