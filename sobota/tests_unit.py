import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        expected = 5
        self.assertEqual(result, expected)
        self.assertEqual(add_numbers(5, 7), 12)
