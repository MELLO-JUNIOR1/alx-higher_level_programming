#!/usr/bin/python3
"""class that inherits from geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """mhm"""

    def __init__(self, width, height):
        """checking and setting"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
