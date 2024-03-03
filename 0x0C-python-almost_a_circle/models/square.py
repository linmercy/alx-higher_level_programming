#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new Square instance."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Getter for size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square instance."""
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square."""
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

