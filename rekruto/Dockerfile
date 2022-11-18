FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV PATH="${PATH}:/root/.poetry/bin"

WORKDIR /backend

COPY poetry.lock pyproject.toml /backend/

RUN pip install poetry

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .