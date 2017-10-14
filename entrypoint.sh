#!/bin/sh
set -e

MANAGE_CMD='python manage.py'

if [ "$1" = 'manage' ]; then
    shift
    exec $MANAGE_CMD $@
elif [ "$1" = 'bootstrap' ]; then
    exec $MANAGE_CMD migrate && $MANAGE_CMD collectstatic --no-input
elif [ "$1" = 'runserver' ]; then
    shift
    exec $MANAGE_CMD runserver_plus 0.0.0.0:8000 $@
elif [ "$1" = 'shell' ]; then
    shift
    exec $MANAGE_CMD shell_plus $@
elif [ "$1" = 'lint' ]; then
    exec flake8 . && mypy .
elif [ "$1" = 'test' ]; then
    shift
    exec pytest $@
elif [ "$1" = 'isort' ]; then
    shift
    exec isort -vb -ac -y -r $@
fi

exec "$@"