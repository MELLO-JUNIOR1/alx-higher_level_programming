#!/usr/bin/python3
"""check the obj"""


def is_kind_of_class(obj, a_class):
    """true is the obj cam from the same class or a sub one"""
    return isinstance(obj, a_class)
