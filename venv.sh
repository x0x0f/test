#!/bin/bash
VERSION=3
/usr/bin/python$VERSION -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
