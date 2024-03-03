import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def test_constructor(self):
        """Test instantiation of Rectangle class."""
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_width_validation(self):
        """Test width attribute validation."""
        with self.assertRaises(ValueError):
            r = Rectangle(-10, 2)

    def test_height_validation(self):
        """Test height attribute validation."""
        with self.assertRaises(ValueError):
            r = Rectangle(10, -2)

    def test_x_validation(self):
        """Test x attribute validation."""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, -1)

    def test_y_validation(self):
        """Test y attribute validation."""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2, 1, -1)

    def test_area(self):
        """Test calculation of rectangle area."""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, mock_stdout):
        """Test display method."""
        r = Rectangle(4, 6)
        expected_output = "####\n" * 6
        r.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()

