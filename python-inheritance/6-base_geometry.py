#!/usr/bin/python3
"""Defines a class BaseGeometry with a method that raises an exception."""


class BaseGeometry:
    """Base class for geometry operations."""

    def area(self):
        """Raises an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
