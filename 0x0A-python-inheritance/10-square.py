#!/usr/bin/python3
"""square class thhat inherits from rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """init"""
    def __init__(self, size):
        """check"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
