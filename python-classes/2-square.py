#!/usr/bin/python3
"""a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """A class that initializes an object with a private attribute size"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
