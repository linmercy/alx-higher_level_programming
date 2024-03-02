import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_constructor(self):
        """Test the constructor of the Rectangle class."""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

    def test_getters_and_setters(self):
        """Test the getters and setters of the Rectangle class."""
        r = Rectangle(10, 2)
        r.width = 5
        r.height = 3
        r.x = 2
        r.y = 1

        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 1)

if __name__ == '__main__':
    unittest.main()

