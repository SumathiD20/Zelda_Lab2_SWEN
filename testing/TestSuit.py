# test_math_operations.py
import unittest
from math_operations import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)  # 2 + 3 = 5
        self.assertEqual(add(-1, 1), 0)  # -1 + 1 = 0
        self.assertEqual(add(0, 0), 0)  # 0 + 0 = 0

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)  # 5 - 3 = 2
        self.assertEqual(subtract(2, 5), -3)  # 2 - 5 = -3
        self.assertEqual(subtract(0, 0), 0)  # 0 - 0 = 0

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)  # 2 * 3 = 6
        self.assertEqual(multiply(-1, 1), -1)  # -1 * 1 = -1
        self.assertEqual(multiply(0, 5), 0)  # 0 * 5 = 0

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)  # 6 / 3 = 2
        self.assertEqual(divide(5, 2), 2.5)  # 5 / 2 = 2.5
        self.assertRaises(ValueError, divide, 5, 0)  # Division by zero raises ValueError

if __name__ == "__main__":
    unittest.main()
