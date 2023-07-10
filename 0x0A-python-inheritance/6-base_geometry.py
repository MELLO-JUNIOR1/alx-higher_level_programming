#!/usr/bin/python3
"""base class"""


class BaseGeometry:
    """raise error area"""
    def area(self):
        raise Exception("area() is not implemented")
