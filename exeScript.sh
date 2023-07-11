#! /bin/bash

python3 train.py
gunicorn -b :$PORT main:app