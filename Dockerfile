FROM python:3.6-alpine as python-base
RUN apk add --no-cache \
        gettext-dev \
        postgresql-dev \
        gcc \
        musl-dev \
        jpeg-dev \
        zlib-dev \
        linux-headers
COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH $PYTHONPATH:code
ENV MYPYPATH $PYTHONPATH:code

RUN apk add --no-cache \
        gettext \
        libpq \
        libjpeg \
        mailcap
COPY --from=python-base /root/.cache /root/.cache
COPY --from=python-base requirements.txt .
RUN pip install -r requirements.txt && rm -rf /root/.cache

WORKDIR /code
COPY . /code/
