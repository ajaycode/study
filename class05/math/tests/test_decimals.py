# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys
from decimal import ROUND_HALF_UP, Decimal

sys.path.append('..\\')
from decimals import *


class TestDecimals(TestCase):

    def test_sort_decimals(self):
        question, answer = sort_decimals ([decimal.Decimal('1.3014'),decimal.Decimal('0.9286'),decimal.Decimal('1.1868'), decimal.Decimal('0.9887')])
        self.assertEqual(r'0.9286,0.9887,1.1868,1.3014', answer)
        question, answer = sort_decimals ([decimal.Decimal('1.3573'),decimal.Decimal('0.237'),decimal.Decimal('.1087'), decimal.Decimal('.1673')])
        self.assertEqual(r'0.1087,0.1673,0.237,1.3573', answer)

    def test_sort_decimals_descending (self):
        question, answer = sort_decimals_descending ([decimal.Decimal('1.5322'),decimal.Decimal('0.3238'),decimal.Decimal('0.160'),decimal.Decimal('1.9656')])
        self.assertEqual(r'1.9656,1.5322,0.3238,0.160', answer)
        question, answer = sort_decimals_descending ([decimal.Decimal('0.2400'),decimal.Decimal('0.3625'),decimal.Decimal('0.4785'),decimal.Decimal('1.6537')])
        self.assertEqual(r'1.6537,0.4785,0.3625,0.2400', answer)

    def test_decimals_multiplication (self):
        __, answer = decimals_multiplication (decimal.Decimal('2.60'), decimal.Decimal('251.647'))
        self.assertEqual(decimal.Decimal('654.28220'), answer)

    def test_decimals_division (self):
        __, answer = decimals_division (decimal.Decimal('22.7665'), decimal.Decimal('8.79'))
        self.assertEqual(decimal.Decimal('2.59005'), answer)
        __, answer = decimals_division (decimal.Decimal('14.6643'), decimal.Decimal('3.87'))
        self.assertEqual(decimal.Decimal('3.78922'), answer)

    def test_decimal_to_fraction (self):
        __, answer = decimal_to_fraction (decimal.Decimal('0.009'))
        self.assertEqual (r'$\frac {9}{1000}$', answer)
        __, answer = decimal_to_fraction (decimal.Decimal('0.039'))
        self.assertEqual (r'$\frac {39}{1000}$', answer)
        __, answer = decimal_to_fraction (decimal.Decimal('0.39'))
        self.assertEqual (r'$\frac {39}{100}$', answer)
        __, answer = decimal_to_fraction (decimal.Decimal('3.9'))
        self.assertEqual (r'$\frac {39}{10}$', answer)

    def test_multiple_decimals_to_fractions (self):
        __, answer = multiple_decimals_to_fractions ([decimal.Decimal('0.008'), decimal.Decimal('0.945'), decimal.Decimal('0.01'), decimal.Decimal('0.831')])
        self.assertEqual(r'$\frac {1}{125}$,$\frac {189}{200}$,$\frac {1}{100}$,$\frac {831}{1000}$', answer)
        __, answer = multiple_decimals_to_fractions ([decimal.Decimal('0.004'), decimal.Decimal('0.326'), decimal.Decimal('0.02'), decimal.Decimal('0.144')])
        self.assertEqual(r'$\frac {1}{250}$,$\frac {163}{500}$,$\frac {1}{50}$,$\frac {18}{125}$', answer)

    def test_decimals_integers_multiplication (self):
        __, answer = decimals_integers_multiplication (decimal.Decimal('0.75'), 36)
        self.assertEqual(decimal.Decimal('27.00'), answer)

    def test_decimals_integers_division (self):
        __, answer = decimals_integers_division (decimal.Decimal('3.39'), 8)
        self.assertEqual(decimal.Decimal('0.42375'), answer)
        __, answer = decimals_integers_division (decimal.Decimal('0.26'), 5)
        self.assertEqual(decimal.Decimal('0.052'), answer)

    def test_integers_decimals_division (self):
        __, answer = integers_decimals_division (81, decimal.Decimal('0.4'))
        self.assertEqual(decimal.Decimal('202.5'), answer)

    def test_percentage_of_whole_numbers (self):
        __, answer = percentage_of_whole_numbers (70, 55)
        self.assertEqual(38.5, answer)

    def test_decimal_as_percentage (self):
        __, answer = decimal_as_percentage (decimal.Decimal('0.948'))
        self.assertEqual(94.8, answer)

    def test_fraction_as_percentage (self):
        __, answer = fraction_as_percentage (Fraction (11, 25))
        self.assertEqual(44.0, answer)
        __, answer = fraction_as_percentage (Fraction (13, 25))
        self.assertEqual(52.0, answer)








if __name__ == '__main__':
    unittest.main()
