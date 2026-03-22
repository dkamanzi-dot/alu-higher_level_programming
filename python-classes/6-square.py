#!/usr/bin/python3
"""This module defines a Square class that supports size,position,printing."""


class Square:
    """Represents a square with size, position, area computation, printing."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square.

        Args:
            size (int): Size of the square (default is 0).
            position (tuple): Position offset for printing (default is (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): New size value to assign.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using `#`, offset by the `position`."""
        if self.__size == 0:
            print()
            return

        # Print newlines for vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each row with leading spaces for horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
