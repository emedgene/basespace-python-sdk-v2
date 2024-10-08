ARG DOCKER_BUILDER_BASE=ubuntu:22.04

FROM $DOCKER_BUILDER_BASE AS package-builder
ARG POETRY_VERSION=1.5.1
ARG POETRY_INSTALLER_CID=385616cd90816622a087450643fba971d3b46d8c
ARG PYENV_GIT_TAG=v2.3.23
ARG PYENV_INSTALLER_CID=86a08ac9e38ec3a267e4b5c758891caf1233a2e4
ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && apt install -y curl \
    git \
    gcc \
    make \
    zlib1g-dev \
    libssl-dev \
    liblzma-dev \
    libffi-dev \
    libsqlite3-dev \
    libncurses5-dev libncursesw5-dev \
    libreadline-dev \
    libbz2-dev

# install pyenv
RUN set -exu; \
    git clone https://github.com/pyenv/pyenv-installer.git pyenv-installer; \
    git --git-dir="pyenv-installer/.git" checkout "$PYENV_INSTALLER_CID"; \
    /pyenv-installer/bin/pyenv-installer; \
    rm -rf pyenv-installer
ENV PATH="$PATH:/root/.pyenv/bin"
RUN pyenv install 3.10 3.11
RUN pyenv global 3.10
ENV PATH="/root/.pyenv/shims:${PATH}"

#install poetry
RUN set -exu; \
    git clone https://github.com/python-poetry/install.python-poetry.org poetry-installer; \
    git --git-dir="poetry-installer/.git" checkout "$POETRY_INSTALLER_CID" ; \
    python poetry-installer/install-poetry.py --version "$POETRY_VERSION"; \
    /root/.local/bin/poetry --version; \
    rm -rf poetry-installer
ENV PATH="$PATH:/root/.local/bin"

WORKDIR /opt/bssh_sdk_2

ARG POETRY_HTTP_BASIC_JFROG_USERNAME
ARG POETRY_HTTP_BASIC_JFROG_PASSWORD
COPY .emgbuild/ .emgbuild/
COPY pyproject.toml Makefile project.mk ./
# populate poetry cache and create poetry.lock
RUN make init EMGBUILD_POETRY_INSTALL=main

COPY bssh_sdk_2 ./bssh_sdk_2
COPY README.md ./
ARG PEP440_VERSION=0.0.1.dev0+local

RUN set -exu; \
    make build; \
    mv ./dist /dist

####################################################
FROM package-builder as tester

ARG POETRY_HTTP_BASIC_JFROG_USERNAME
ARG POETRY_HTTP_BASIC_JFROG_PASSWORD
ARG PYTHON_VERSION=3.10
ARG ELASTICSEARCH_SDK_VERSION=6

RUN pyenv local $PYTHON_VERSION
RUN if [ "$ELASTICSEARCH_SDK_VERSION" ]; then poetry add "elasticsearch=^$ELASTICSEARCH_SDK_VERSION"; fi

RUN make init

COPY .coveragerc .ruff.toml ./
COPY config ./config
COPY tests ./tests


RUN make check
CMD make test

