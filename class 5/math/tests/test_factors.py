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

        self.assertEqual(4290, least_common_multiple([330, 65, 15]))
        self.assertEqual(1440, least_common_multiple([45,32,16]))
        self.assertEqual(5208, least_common_multiple([31,24,14]))
        self.assertEqual(46512, least_common_multiple([323,272,153]))
        self.assertEqual((1530, 34), lcm_and_hcf([306, 170, 170]))
        self.assertEqual((6930, 9), lcm_and_hcf([90, 126, 99]))
        self.assertEqual(12, pole_spacing([60,36,84]))
        self.assertEqual((8,3,2), stamp_distribution([24,16]))
        self.assertEqual((6,3,5), stamp_distribution([18,30]))
        self.assertEqual(8, march_past([32, 40]))
        self.assertEqual (50, building_age(50))
