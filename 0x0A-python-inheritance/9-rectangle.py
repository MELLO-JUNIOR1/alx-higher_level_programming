#!/usr/bin/python3
"""class that inhirit from geometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """"return the area"""
        return self.__height * self.__width

    def __str__(self):
        """return info"""
        word = "[" + type(self).__name__ + "] "
        word += str(self.__width) + "/" + str(self.__height)
        return word
