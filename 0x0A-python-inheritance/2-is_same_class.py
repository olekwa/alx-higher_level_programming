#!/usr/bin/python3
"""
========================================
Defin a module with method is_same_class
========================================
"""


def is_same_class(obj, a_class):
    """This checks and return True if an object is an instance of a class"""

    return type(obj) is a_class
