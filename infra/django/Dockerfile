FROM python:3.6-stretch
ENV PYTHONUNBUFFERED 1

WORKDIR /code

ARG REQUIREMENTS_FILE=base.txt
COPY requirements/ /code/
RUN pip install -r $REQUIREMENTS_FILE && rm *.txt

COPY src /code/
ENV PYTHONPATH=/code/src:$PYTHONPATH
