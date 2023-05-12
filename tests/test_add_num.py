#!/usr/bin/python3
import unittest
from add_num import add_num

class TestAddNum(unittest.TestCase):

    def test_add_num(self):
        self.assertEqual(add_num(1, 2), 3)
        self.assertEqual(add_num(0, 0), 0)
        self.assertEqual(add_num(-1, 1), 0)
        self.assertEqual(add_num(10, -5), 5)

if __name__ == '__main__':
    unittest.main()
