#!/usr/bin/python3
"""
=============================================
This dedines module with method inherits_from
=============================================
"""


def inherits_from(obj, a_class):
    """This method checks and returns True if an object is an instance of a class
    that inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
