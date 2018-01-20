# gifz-api

Create super user with username admin, he will be author of
populate_db_from_dir gifs.

```
docker-compose -f dev.yml run --rm django python manage.py migrate
docker-compose -f dev.yml run --rm django python manage.py createsuperuser
docker-compose -f dev.yml run --rm django python manage.py populate_db_from_dir ./gifs_db/
```
