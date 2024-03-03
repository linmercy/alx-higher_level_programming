import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io

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

    def test_display(self):
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(60, 70, 80, 90, 100)
        self.assertEqual(r.id, 60)
        self.assertEqual(r.width, 70)
        self.assertEqual(r.height, 80)
        self.assertEqual(r.x, 90)
        self.assertEqual(r.y, 100)

    def test_update_kwargs(self):
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(id=60, width=70, height=80, x=90, y=100)
        self.assertEqual(r.id, 60)
        self.assertEqual(r.width, 70)
        self.assertEqual(r.height, 80)
        self.assertEqual(r.x, 90)
        self.assertEqual(r.y, 100)

if __name__ == '__main__':
    unittest.main()

