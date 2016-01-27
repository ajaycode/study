# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys, decimal
from decimal import ROUND_HALF_UP

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







if __name__ == '__main__':
    unittest.main()
