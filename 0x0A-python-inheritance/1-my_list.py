#!/usr/bin/python3
"""
====================================================
This defines an inheritance module with class MyList
====================================================
"""


class MyList(list):
    """Implememt class with method print_sorted"""
    pass

    def print_sorted(self):
        """Method to print sorted list in ascending order."""

        print(sorted(list(self)))
