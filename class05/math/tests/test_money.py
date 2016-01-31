# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys
from decimal import ROUND_HALF_UP, Decimal

sys.path.append('..\\')
from money import *


class TestMoney(TestCase):

    def test_purchase_costs_input_costs_selling_price(self):
        question, answer = purchase_costs_input_costs_selling_price (4864, 964, 7398)
        self.assertEqual(1570, answer)

    def test_cost_input_loss (self):
        question, answer = cost_input_loss (840, 160, 150)
        self.assertEqual(850, answer)

    def test_selling_price_profit (self):
        q, a = selling_price_profit (9104, 1051)
        self.assertEqual(8053, a)

    def test_bulk_purchase_with_unit_loss (self):
        q, a = bulk_purchase_with_unit_loss (1344, 48, 2)
        self.assertEqual(1248, a)
        q, a = bulk_purchase_with_unit_loss (1295, 37, 9)
        self.assertEqual(962, a)

    def test_bulk_purchase_with_unit_profit (self):
        q, a = bulk_purchase_with_unit_profit (1872, 36, 11)
        self.assertEqual(2268, a)

    def test_unit_profit_on_bulk_sale (self):
        q, a = unit_profit_on_bulk_sale (162, 216, 18)
        self.assertEqual(3.0, a)


if __name__ == '__main__':
    unittest.main()
