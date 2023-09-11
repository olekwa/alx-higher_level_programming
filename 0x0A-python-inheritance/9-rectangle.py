#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
========================================
This is a module with class BaseGeometry
========================================
"""


class Rectangle(BaseGeometry):
    """This is a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """This is a method that initialized the attrubutes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This method redefines an area method in a parent class"""

        return self.__width * self.__height

    def __str__(self):
        """__str__ module for return the next string"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
