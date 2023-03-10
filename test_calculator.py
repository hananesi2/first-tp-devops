"""Unit tests for calculator.py"""

import unittest
import calculator

class TestCalculator(unittest.TestCase):
    """Tests for the calculator functions"""

    def test_add(self):
        """Test the add function"""
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(-1, 1), -2)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiply function"""
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(-1, 1), -1)
        self.assertEqual(calculator.multiply(-1, -1), 1)

    def test_divide(self):
        """Test the divide function"""
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(-1, 1), -1)
        self.assertEqual(calculator.divide(-6, -3), 2)
        with self.assertRaises(ValueError):
            calculator.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
