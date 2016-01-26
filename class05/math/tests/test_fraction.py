from unittest import TestCase

__author__ = 'Ajay'
import sys

sys.path.append('..\\')
from fraction import *


class TestFraction(TestCase):
    def test_fraction(self):
        self.assertEqual(r'$\frac {2}{3}$', printable_fraction(2, 3))
        self.assertEqual(r'$\frac {12}{3}$', printable_fraction(12, 3))
        self.assertEqual(r'$\frac {2}{403}$', printable_fraction(2, 403))

    def test_fractions_sum (self):
        #self.assertEqual()
        pass
