FROM python:3.6-stretch
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ARG REQUIREMENTS_FILE
COPY requirements/ /code/
RUN pip install -r $REQUIREMENTS_FILE && rm *.txt

COPY src /code/
COPY tests /code/

WORKDIR /code/src/
ENV PYTHONPATH=/code/src:/code/tests:$PYTHONPATH
