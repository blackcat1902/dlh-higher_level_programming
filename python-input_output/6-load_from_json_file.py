#!/usr/bin/python3
"""Module for loading a JSON file and creating a Python object from it."""

import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
