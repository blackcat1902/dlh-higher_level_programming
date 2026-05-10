#!/usr/bin/env python3
"""
task_02_csv.py
Convert CSV data to JSON format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert CSV file data to JSON format and save it to data.json.

    Args:
        csv_filename (str): Name of the CSV file to read

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        data = []

        with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except (FileNotFoundError, IOError, csv.Error):
        return False
