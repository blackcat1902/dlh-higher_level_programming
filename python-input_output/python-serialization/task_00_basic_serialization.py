!/usr/bin/env python3
"""
task_00_basic_serialization.py
Basic serialization module using JSON
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize
        filename (str): Output JSON file name
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): Input JSON file name

    Returns:
        dict: Deserialized Python dictionary
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
