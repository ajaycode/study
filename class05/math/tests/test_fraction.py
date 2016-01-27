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
        number1 = Fraction (25,3)
        number2 = Fraction (47,5)
        question, answer = mixed_fractions_sum(number1, number2)
        self.assertEqual(r'$17\frac {11}{15}$', answer )

    def test_mixed_fraction_difference (self):
        number1 = Fraction(77,9)
        number2 = Fraction (43,7)
        question, answer = mixed_fractions_difference(number1, number2)
        self.assertEqual(r'$2\frac {26}{63}$', answer )
        number1 = Fraction (23,6)
        number2 = Fraction (7,3)
        question, answer = mixed_fractions_difference(number1, number2)
        self.assertEqual(r'$1\frac {1}{2}$', answer )

    def test_mixed_fraction_multiplication (self):
        number1 = Fraction(65,8)
        number2 = Fraction (2,1)
        question, answer = mixed_fractions_multiplication(number1, number2)
        self.assertEqual(r'$16\frac {1}{4}$', answer )
        number1 = Fraction (29,3)
        number2 = Fraction (1,6)
        question, answer = mixed_fractions_multiplication(number1, number2)
        self.assertEqual(r'$1\frac {11}{18}$', answer )

    def test_fractions_division (self):
        number1 = Fraction(8,7)
        number2 = Fraction (9,8)
        question, answer = fractions_division(number1, number2)
        self.assertEqual(r'$1\frac {1}{63}$', answer )
        number1 = Fraction (2,1)
        number2 = Fraction (7,9)
        question, answer = fractions_division(number1, number2)
        self.assertEqual(r'$2\frac {4}{7}$', answer )

    def test_fractions_division_by_whole_number (self):
        number1 = Fraction(1,1)
        number2 = 4
        question, answer = fractions_division_by_whole_number(number1, number2)
        self.assertEqual(r'$\frac {1}{4}$', answer )
        number1 = Fraction (2,1)
        number2 = Fraction (9)
        question, answer = fractions_division_by_whole_number(number1, number2)
        self.assertEqual(r'$\frac {2}{9}$', answer )

    def test_whole_number_by_fractions_division (self):
        question, answer = whole_number_by_fractions_division (5, Fraction (5,2))
        self.assertEqual(r'$\frac {2}{1}$', answer )
        question, answer = whole_number_by_fractions_division (3, Fraction (5,9))
        self.assertEqual(r'$\frac {27}{5}$', answer )

    def test_mixed_fractions_division (self):
        question, answer = mixed_fractions_division (Fraction(16,3), Fraction (7,2))
        self.assertEqual(r'$1\frac {11}{21}$', answer )
        question, answer = mixed_fractions_division (Fraction(17,4), Fraction (5,2))
        self.assertEqual(r'$1\frac {7}{10}$', answer )




if __name__ == '__main__':
    unittest.main()
