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

    def test_bodmas_decimals (self):
        question, answer = bodmas_decimals ("0.14 * 11.90 / 1.70 * 0.7 - 0.2")
        self.assertEqual(0.486, answer)
        question, answer = bodmas_decimals ("0.43 + 0.2 * 0.4 + 0.6 * 0.2")
        self.assertEqual(0.63, answer)
        question, answer = bodmas_decimals ("2.9 + 0.7 * 1.60 / 0.32 - 0.9")
        self.assertEqual(5.5, answer)

    def test__bodmas_fractions_solver (self):
        a = bodmas_fractions_solver([Fraction (200, 2),Fraction (1,4),Fraction (2,3),Fraction (1,3),Fraction (2,3)], ["/", "*", "+", "-"])
        self.assertEqual(Fraction (799, 3), a)
        a = bodmas_fractions_solver([Fraction (2,3),Fraction (5,4),Fraction (2,3),Fraction (5, 12),Fraction (7,8)], ["*", "/", "+", "-"])
        self.assertEqual(Fraction (19, 24), a)
        a = bodmas_fractions_solver([Fraction (9,7),Fraction (5,3),Fraction (8,5),Fraction (7,3),Fraction (1,2)], ["/", "+", "/", "+"])
        self.assertEqual(Fraction (137, 70), a)


if __name__ == '__main__':
    unittest.main()
