#!/bin/bash
source .venv/bin/activate
export PYTHONPATH=.
python -m pytest -v test.py -p no:warnings
