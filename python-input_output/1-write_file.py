#!/usr/bin/python3
"""Module for writing a string to a text file a UTF-8 text file."""


def write_file(filename="", text=""):
    """A function that writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text) 
