#!/usr/bin/env bash

env_name=faster

if [ -e "${PYENV_ROOT}/versions/${env_name}" ]; then
    echo "Activating virtualenv ${env_name}"
    . ${PYENV_ROOT}/versions/${env_name}/bin/activate
fi

pip install -r ./backend/requirements.txt
npm install --prefix ./frontend