#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
==========================================
This defines a module with class Rectangle
==========================================
"""


class Rectangle(BaseGeometry):
    """This is a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
