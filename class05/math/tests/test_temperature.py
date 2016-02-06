# ..\tests>python test_fraction.py

import unittest
from unittest import TestCase
__author__ = 'Ajay'
import sys
from decimal import ROUND_HALF_UP, Decimal

sys.path.append('..\\')
from temperature import *


class TestTemperature(TestCase):

    def test_celsius_from_fahrenheit(self):
        question, answer = celsius_from_fahrenheit (60)
        self.assertEqual("{}{}C".format (15.6, u'\N{DEGREE SIGN}'), answer)
        question, answer = celsius_from_fahrenheit (80)
        self.assertEqual("{}{}C".format (26.7,u'\N{DEGREE SIGN}'), answer)

    def test_fahrenheit_from_celsius (self):
        q, a = fahrenheit_from_celsius (60)
        self.assertEqual("140.0{}F".format (u'\N{DEGREE SIGN}'), a)
        q, a = fahrenheit_from_celsius (80)
        self.assertEqual("176.0{}F".format (u'\N{DEGREE SIGN}'), a)



if __name__ == '__main__':
    unittest.main()
