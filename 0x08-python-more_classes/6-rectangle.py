#!/usr/bin/python3
"""class define the area and perimeter of rectangle"""


class Rectangle:
    """ init method """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ setting value to width and height attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """return width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting value above 0 to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return heigth"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting value above 0 to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (2 * (self.__height + self.__width))

    def __str__(self):
        """printing a set of # dependin on height and width"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        diz = []
        for i in range(self.__height):
            [diz.append("#") for j in range(self.__width)]
            if i != self.__height - 1:
                diz.append("\n")
        return ("".join(diz))

    def __repr__(self):
        """ return the values and class name"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """return a sentence whule deleting"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
