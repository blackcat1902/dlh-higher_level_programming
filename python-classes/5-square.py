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
        self.size =size


    @property
    def size(self):
        """property  to retrieve it"""
        return self.__size

        
    @size.setter
    def size (self, value):
        """ property setter to set it """

        if not isinstance(value, int):
            raise TypeError ("size must be an integer")
        if value < 0:
            raise ValueError ("size must be >= 0")
        self.__size = value
    def area(self):
        """ returns the current area of the square """
        return self.__size**2
    def my_print(self):
        """ Public instance method  that prints in stdout the square with the character # """

        if self.__size == 0:
            print ()
            return 
        for i in range (self.__size):
            print ("#" * self.__size)
