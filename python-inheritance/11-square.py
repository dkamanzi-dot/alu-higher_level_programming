#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
