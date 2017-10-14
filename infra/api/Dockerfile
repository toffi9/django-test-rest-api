FROM python:3.6
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ARG REQUIREMENTS_FILE
COPY requirements/ /code/
RUN pip install -r $REQUIREMENTS_FILE && rm *.txt

COPY django_test_rest_api /code/
COPY tests /code/
COPY manage.py /code/
