#!/usr/bin/python3
"""This module defines a Square class with a private size attribute."""


class Square:
    """Square class with private size attribute."""

    def __init__(self, size):
        """Initialize the square with a private size attribute.

        Args:
            size (int): The size of the square (no validation required here).
        """
        self.__size = size
