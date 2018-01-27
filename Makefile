COMPOSE_FILE?=dev.yml
BASE=docker-compose -f $(COMPOSE_FILE)
RUN_DJANGO = $(BASE) run --rm django
RUN_DJANGO_NO_DEPS = $(BASE) run --rm --no-deps django

lint:
	$(RUN_DJANGO_NO_DEPS) flake8 .
	$(RUN_DJANGO_NO_DEPS) mypy .

isort:
	$(RUN_DJANGO_NO_DEPS) isort -c -vb -r .

test:
	$(RUN_DJANGO) pytest -vv
