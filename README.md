# FastAPI + React

A simple frontend+backend app

## Prerequisites
- Python v.3
- Node.js v.24
- Docker compose v.2

## Setup development environment
1. (optional) Create a virtual environment for python and activate it. The repository contains a [pyenv](https://github.com/pyenv/pyenv) version file that expects a virtual environment named `faster`.
    - `pyenv install 3.13`
    - `pyenv virtualenv 3.13 faster`
2. Run `./install-deps.sh` to install dependencies for both frontend and backend.

## Run development mode

Run `docker compose up -d`.

The servises will be exposed as follows:
- frontend: http://localhost:5173
- backend: http://localhost:8000 