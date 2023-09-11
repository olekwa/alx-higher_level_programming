#!/usr/bin/python3
"""
=============================================
This defines a module with class BaseGeometry
=============================================
"""


class BaseGeometry:
    """Thi is a BaseGeometry class"""

    def area(self):
        """This method is used  for calculated area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method is used to validate if a num is integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
