from unittest import TestCase

__author__ = 'Ajay'
from factors import *


class TestFactors(TestCase):
    def test_factors(self):
        self.assertEqual([673],   factors (673))
        self.assertEqual([3,11,13], factors (429))
        self.assertEqual([167, 334, 501, 668, 835], multiples (167, 5))
        self.assertEqual([150, 300, 450, 600], multiples (150, 4))
        self.assertEqual(False,  is_prime(6))
        self.assertEqual(True,  is_prime(11))
        self.assertEqual(False, is_prime(4))
