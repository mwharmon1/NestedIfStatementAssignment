"""Author: Michael Harmon
   Last Date Modified: 9/18/2019
   Description: These tests will test the calculate_order
   function to ensure the correct value is being returned after
   calculation of the price, cash and percent coupon."""

import unittest
from store import coupon_calculations as cc


class MyTestCase(unittest.TestCase):
    # Test Set 1
    def test_price_under_10_test_1(self):
        self.assertEqual(cc.calculate_order(9.00, 5.00, .10), 9.77)

    def test_price_under_10_test_2(self):
        self.assertEqual(cc.calculate_order(8.00, 5.00, .15), 8.65)

    def test_price_under_10_test_3(self):
        self.assertEqual(cc.calculate_order(7.00, 5.00, .20), 7.65)

    def test_price_under_10_test_4(self):
        self.assertEqual(cc.calculate_order(6.00, 10.00, .10), 2.13)

    def test_price_under_10_test_5(self):
        self.assertEqual(cc.calculate_order(5, 10.00, .15), 1.45)

    def test_price_under_10_test_6(self):
        self.assertEqual(cc.calculate_order(4, 10.00, .20), 0.86)


if __name__ == '__main__':
    unittest.main()

"""Each unit test is testing the different possible 
scenarios that could take place with the calculate_order 
function, passing in different prices with different combinations
of the coupons.
"""