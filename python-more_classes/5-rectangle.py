#!/usr/bin/python3
"""Defines a Rectangle class"""

class Rectangle:
    """a class Rectangle that defines a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ property  to retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter  to set it """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ property  to retrieve it """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter  to set it """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ that returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ that returns the rectangle perimeter """
        if self.__width == 0  or self.__height == 0:
            return 0
        return  2 * (self.__width + self.__height)

    def __str__(self):
        """ print the rectangle with the character # """
        if self.__width == 0 or self.__height == 0 :
            return ""
        row = []
        for i in range(self.__height):
            row.append("#" * self.__width)
        return "\n".join(row)
        
    def __repr__(self):
        """ should return a string representation of the rectangle to be able to recreate a new instance by using eval"""
        return "Rectangle({}, {})".format(self.__width,  self.__height)

    def __del__(self):
        """ prints a message when an instance of Rectangle is deleted """
         print ("Bye rectangle...")