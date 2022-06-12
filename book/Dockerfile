# pull official base image
FROM python:3.10.5-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk add --update --no-cache postgresql-client

# Install individual dependencies
# so that we could avoid install extra packages
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy project
COPY . .

RUN adduser -D user
USER user