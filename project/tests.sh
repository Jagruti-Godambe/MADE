#!/bin/bash
pip3 install --upgrade pip
pip3 install -r /Users/jagrutigodambe/MADE/project/requirements.txt
python3 /Users/jagrutigodambe/MADE/project/pipeline.py
python -m unittest ./Users/jagrutigodambe/MADE/project/test_pipeline.py