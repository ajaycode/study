# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys

sys.path.append('..\\')
from simplification_of_numerical_expressions import *


class TestSimplification(TestCase):

    def test_bodmas_integers(self):
        question, answer = bodmas_integers ("72 + 22 / 22 * 5 + 6 + 13")
        self.assertEqual(96.0, answer)
        question, answer = bodmas_integers ("92 - 15 * 15 - 6 / 2 * 14")
        self.assertEqual(-175, answer)



if __name__ == '__main__':
    unittest.main()
