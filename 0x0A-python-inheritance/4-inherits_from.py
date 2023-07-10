#!/usr/bin/python3
"""check funtion for obj comming from a sub class"""


def inherits_from(obj, a_class):
    """true if obj cam from a sub , false if it cam from the origin"""
    return isinstance(obj, a_class) and not type(obj) == a_class
