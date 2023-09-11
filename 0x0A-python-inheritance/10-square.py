#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
========================================
This is a module with class BaseGeometry
========================================
"""


class Square(Rectangle):
    """The Square module that inherits from Rectangle which inherits BaseGeometry"""

    def __init__(self, size):
        """This is a method that initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """The area of the rectangle"""

        return self.__size ** 2
