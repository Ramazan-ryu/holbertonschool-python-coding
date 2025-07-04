#!/usr/bin/python3
"""a class Square that defines a square by: (based on 0-square.py)"""


class Square:
    """A class that initializes an object with a private attribute size"""

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size * self.__size
