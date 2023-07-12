#!/usr/bin/python3
""",h,"""


def append_after(filename="", search_string="", new_string=""):
    """appending"""
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fl:
        fl.write(text)
