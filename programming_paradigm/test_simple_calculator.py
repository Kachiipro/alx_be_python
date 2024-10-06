import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-14, -78), -92)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtraction method."""

        self.assertEqual(self.calc.subtract(9, 14), -5)
        self.assertEqual(self.calc.subtract(-3, 4), -7)
        self.assertEqual(self.calc.subtract(9, -14), 23)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(9, 5), 45)
        self.assertEqual(self.calc.multiply(-9, 5), -45)
        self.assertEqual(self.calc.multiply(9, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_division(self):
        """Test the multiplication method."""

        self.assertEqual(self.calc.divide(8, 2), 4)
        self.assertEqual(self.calc.divide(8, -8), -1)
        self.assertEqual(self.calc.divide(0, 2), 0)
        self.assertEqual(self.calc.divide(8, 0), None)
