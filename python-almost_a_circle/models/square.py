#!/usr/bin/python3
"""Module for the Square class that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance with size, x, y and id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size that assigns both width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns arguments to each attribute in order: id, size, x, y."""
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square instance."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns string representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
