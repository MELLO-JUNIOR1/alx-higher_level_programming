#!/usr/bin/python3
"""function that write obj in a file"""
import json


def save_to_json_file(my_obj, filename):
    """write"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
