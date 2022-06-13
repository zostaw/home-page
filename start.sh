#!/bin/bash
MAIN_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )


cd $MAIN_DIR/venv/bin/

ps -ef | grep "$MAIN_DIR" | grep -v grep | grep -v $! | awk '{print $2}' | xargs kill -9 &>/dev/null

source ./activate
cd $MAIN_DIR
export FLASK_APP=main.py
flask run --host 0.0.0.0 --port 8000