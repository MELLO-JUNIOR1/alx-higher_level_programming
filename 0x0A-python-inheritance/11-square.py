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

    def __str__(self):
        """return info"""
        word = "[" + type(self).__name__ + "] "
        word += str(self.__size) + "/" + str(self.__size)
        return word
