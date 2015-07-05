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
        self.assertEqual([2, 19, 23], all_factors(874))
        self.assertEqual([2, 2, 103], all_factors(412))
        self.assertEqual(("Factors = [17, 19, 23, 29]. Product = 215441"), consecutive_primes(17, 4))
        self.assertEqual(("Factors = [11, 13]. Product = 143"), consecutive_primes(11, 2))
        self.assertEqual(12, highest_common_factor([36, 48]))
        self.assertEqual(6, highest_common_factor([24, 30, 90]))
        self.assertEqual(1, highest_common_factor([13, 21, 17]))
        self.assertEqual(4, highest_common_factor([72, 104, 92]))
