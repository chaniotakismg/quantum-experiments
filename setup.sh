#!/usr/bin/env bash
export VENV=./venv
if [[ ! -d "$venv" ]]
then
    python3 -m pip install --user --upgrade pip
    python3 -m pip install --user virtualenv
    python3 -m venv ./venv
    source ./venv/bin/activate
    pip3 install -r ./requirements.txt
    deactivate
fi

IBM=./ibm.conf
if [[ ! -f "$IBM" ]]; then
    # shellcheck disable=SC2028
    echo '[IBM]\ntoken=<replace_me_with_IBMQ_token>' > $IBM
fi

source ./venv/bin/activate