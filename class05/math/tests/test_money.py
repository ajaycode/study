# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys
from decimal import ROUND_HALF_UP, Decimal

sys.path.append('..\\')
from money import *


class TestDecimals(TestCase):

    def test_purchase_costs_input_costs_selling_price(self):
        question, answer = purchase_costs_input_costs_selling_price (4864, 964, 7398)
        self.assertEqual(1570, answer)

    def test_cost_input_loss (self):
        question, answer = cost_input_loss (840, 160, 150)
        self.assertEqual(850, answer)

    def test_selling_price_profit (self):
        q, a = selling_price_profit (9104, 1051)
        self.assertEqual(8053, a)

if __name__ == '__main__':
    unittest.main()
