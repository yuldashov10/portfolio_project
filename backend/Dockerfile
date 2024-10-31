FROM python:3.10-slim AS python-base

ENV ENVIRONMENT="development"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_ROOT_USER_ACTION=ignore \
    PIP_DEFAULT_TIMEOUT=100

ENV POETRY_VERSION="1.8.3" \
    POETRY_CORE_VERSION="1.9.0" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_HOME="/opt/poetry" \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"
ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base AS builder

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - --version "$POETRY_VERSION" \
    && pip install "poetry-core==$POETRY_CORE_VERSION" \
    && poetry --version

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-dev

FROM python-base AS base

WORKDIR $PYSETUP_PATH

COPY --from=builder $POETRY_HOME $POETRY_HOME
COPY --from=builder $PYSETUP_PATH $PYSETUP_PATH
COPY ./backend/entrypoint.sh /entrypoint.sh

RUN poetry install

WORKDIR /app
COPY . /app

EXPOSE 8000

RUN chmod +x /entrypoint.sh \
    && mkdir -p /app/media /app/static \
    && chmod +x /app/media /app/static

WORKDIR /app/backend/

ENTRYPOINT ["/entrypoint.sh"]
