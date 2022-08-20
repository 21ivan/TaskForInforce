FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY App /App

WORKDIR /App
EXPOSE 8000

RUN python3 -m venv py && \
    source py/bin/activate && \
    py/bin/pip install --upgrade pip &&\
    py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home App

ENV PATH="/py/bin:$PATH"

USER app

