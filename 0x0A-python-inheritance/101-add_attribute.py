#!/usr/bin/python3


"""
===========================================================
Defines a function that adds attributes to objects.
=========================================================
"""


def add_attribute(obj, att, value):
    """This will add a new attribute to an object if"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
