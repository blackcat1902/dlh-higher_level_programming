#!/usr/bin/python3
"""This Modules defines a square class"""



class Square:
    """ Represents a square """
    
    def __init__(self, size=0):
        """ Args:
            size(int): The size of the square
            size must be an integer
            size must be >= 0
        """
    def size(self):
        """property  to retrieve it"""
        return self.__size
    def size (self, value):
        """ property setter to set it """

        if not isinstance(size, int):
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
    def area(self):
        """ returns the current area of the square """
        return self.__size**2
    