#!/usr/bin/python3

"""
0x08. Python - More Classes and Objects
"""


class Rectangle:
    """The class Rectangle
    Private instance attribute: width:
        - property def width(self): to retrieve it
        - property setter def width(self, value): to set it:
            # width must be an integer, otherwise raise a TypeError
            exception with the message width must be an integer
            # if width is less than 0, raise a ValueError exception
                with the message width must be >= 0

    Private instance attribute: height:
                same thing goes exactly as width.
    Public class attribute number_of_instances:
        - Initialized to 0
        - Incremented during each new instance instantiation
        - Decremented during each instance deletion
    Public class attribute print_symbol:
        - Initialized to #
        - Used as symbol for string representation
        - Can be any type
    Instantiation with optional width and height:
    def __init__(self, width=0, height=0):
    Public instance method: def area(self): that returns the rectangle area
    Public instance method: def perimeter(self): that returns perimeter:
        - if width or height is equal to 0, perimeter is equal to 0
    print() and str() should print the rectangle with the character #:
        - if width or height is equal to 0, return an empty string
    repr() should return a string representation of the rectangle to be able
    to recreate a new instance by using eval()
    Print the message Bye rectangle... (... being 3 dots not ellipsis) when
    an instance of Rectangle is deleted
    Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest
    rectangle based on the area
        - rect_1 must be an instance of Rectangle, otherwise raise a TypeError
                exception, message rect_1 must be an instance of Rectangle
        - rect_2 must be an instance of Rectangle, otherwise raise a TypeError
                exception, message rect_2 must be an instance of Rectangle
        - Returns rect_1 if both have the same area value
    Class method def square(cls, size=0): that returns a new Rectangle instance
    with width == height == size
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__ dunder
        Arguments:
            width : the width of rectangle
            height : the height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
                Args:
            value: The new width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
                Args:
            value: The new height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area method"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter method"""
        if self.__width == 0 or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __repr__(self):
        """__repr__ dunder"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        """__str__ dunder"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([str(self.print_symbol) * self.__width] *
                         self.__height)

    def __del__(self):
        """__del__ dunder"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2
            else:
                return rect_1

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
