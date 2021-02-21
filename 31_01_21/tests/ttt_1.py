import unittest
from try_test import division, hello


class TestTry(unittest.TestCase):
    def test_division(self):
        self.assertEqual(division(1, 1), 1, 'Should be 1')
        self.assertEqual(division(0, 1), 0, 'Should be 0')
        self.assertEqual(division(1, 2), 0.5, 'Should be 0.5')

        self.assertRaises(ZeroDivisionError, division, 1, 0)

    def test_hello(self):
        self.assertEqual(hello(), 'Hello', 'wrong message')



