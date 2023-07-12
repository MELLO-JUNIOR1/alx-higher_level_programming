#!/usr/bin/python3
"""function thatcreates an Object from a “JSON file” """
import json


def load_from_json_file(filename):
    """open with r"""
    with open(filename) as f:
        return json.load(f)
