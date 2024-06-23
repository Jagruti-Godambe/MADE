#!/bin/bash

pip3 install --upgrade pip
pip3 install -r ./project/requirements.txt
python3 ./project/pipeline.py
python -m unittest ./project/test_pipeline.py
