#!/usr/bin/python3
"""Module for appending a string at the end of a UTF-8 text file."""


def append_write(filename="", text=""):
    """A function that appends a string at the end of a text file (UTF8)."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)