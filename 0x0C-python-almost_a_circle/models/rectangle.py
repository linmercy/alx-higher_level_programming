#!/usr/bin/python3
"""Defines the Rectangle class."""

class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id if id is not None else 0

    def __str__(self):
        """Returns string representation of Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def area(self):
        """Computes the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Displays the rectangle with '#' characters."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the Rectangle instance."""
        if args:
            attrs = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

