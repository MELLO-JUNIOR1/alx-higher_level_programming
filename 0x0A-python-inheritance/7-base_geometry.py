#!/usr/bin/python3
""" geometry module """


class BaseGeometry:
    """getmetry class"""

    def area(self):
        """raise err"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check and raise error if so"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
