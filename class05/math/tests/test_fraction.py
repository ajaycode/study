# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys

sys.path.append('..\\')
from fraction import *


class TestFraction(TestCase):
    def test_printable_fraction(self):
        self.assertEqual(r'$\frac {2}{3}$', printable_fraction(2, 3))
        self.assertEqual(r'$\frac {12}{3}$', printable_fraction(12, 3))
        self.assertEqual(r'$\frac {2}{403}$', printable_fraction(2, 403))

    def test_printable_fraction_from_fraction (self):
        self.assertEqual(r'$\frac {2}{403}$', printable_fraction_from_fraction(Fraction(2, 403)))

    def test_sort_unlike_fractions(self):
        question, answer = sort_unlike_fractions ([Fraction(1,2), Fraction (3,4), Fraction (2,3), Fraction (15,16)])
        self.assertEqual(r'$\frac {1}{2}$,$\frac {2}{3}$,$\frac {3}{4}$,$\frac {15}{16}$', answer)
        question, answer = sort_unlike_fractions ([Fraction(1,2), Fraction (3,4), Fraction (2,3), Fraction (15,16)], ascending=False)
        self.assertEqual(r'$\frac {15}{16}$,$\frac {3}{4}$,$\frac {2}{3}$,$\frac {1}{2}$', answer)

    def test_fractions_sum (self):
        self.assertEqual(3, 2+1)
        pass

    def test_mixed_fraction_sum (self):
        number1 = Fraction(25,3)
        number2 = Fraction (33,4)
        question, answer = mixed_fractions_sum(number1, number2)
        self.assertEqual(r'$16\frac {7}{12}$', answer )

if __name__ == '__main__':
    unittest.main()
