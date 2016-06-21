import unittest
from unittest import TestCase
import sys

__author__ = 'Ajay'
sys.path.append ('..\\..\\')  #path, if this tests are executed as python tests/test_factors.py
sys.path.append ('..\\..\\..\\') # path, if these tests are executed from tests directory as python test_factors.py
from class06.math.factors06 import *


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
        self.assertEqual(1260, least_common_multiple([4,5,7,9]))
        self.assertEqual(26180, least_common_multiple([4,5,7,11,17]))
        self.assertEqual((1530, 34), lcm_and_hcf([306, 170, 170]))
        self.assertEqual((6930, 9), lcm_and_hcf([90, 126, 99]))
        self.assertEqual(12, pole_spacing([60,36,84]))
        self.assertEqual((8,3,2), stamp_distribution([24,16]))
        self.assertEqual((6,3,5), stamp_distribution([18,30]))
        self.assertEqual(8, march_past([32, 40]))
        self.assertEqual (50, building_age(50))
        self.assertEqual((123, [6,8,10]), chocolate_distribution ([6, 8, 10], 3))
        self.assertEqual(36,  students_in_class([6, 9, 12, 18]))
        self.assertEqual((120, [4,3]), students_running_circles([30, 40]))
        self.assertEqual((60, [5,4]), students_running_circles([12, 15]))
        self.assertEqual((7, [3,5,7] ),  journey_time_minimum_hours([21, 35, 49]))
        self.assertEqual((2, [3,4,5]),   journey_time_minimum_hours([6, 8, 10]))
        self.assertEqual(2, containers_hcf([38, 1160]))
        self.assertEqual(16, containers_hcf([144, 176]))

if __name__ == '__main__':
    unittest.main()