#!/usr/bin/python3
"""Funtion adds new attributes """


def add_attribute(obj, att, value):
    """setting a check"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
