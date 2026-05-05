
#!/usr/bin/python3
"""
This module defines a Square class.
The Square class is defined with a private size attribute.
"""


class Square:
    """
    This class defines a square with a private size attribute.
    """

    def __init__(self, size):
        """
        Initializes a Square instance with a given size.

        Args:
            size: The size of the square (no type or value validation).
        """
        self.__size = size
