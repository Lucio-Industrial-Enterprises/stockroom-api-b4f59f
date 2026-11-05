import unittest

from warehouse.rates import shipping_quote


class StandardRateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", service="standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")


class ExpressRateTests(unittest.TestCase):
    def test_express_local(self):
        # standard local: 5.0 + 1.5*2 = 8.0; express adds 7.0 → 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # standard regional: 8.0 + 1.5*2 = 11.0; express adds 7.0 → 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # 8.0 + 1.5*1.5 + 7.0 = 17.25
        self.assertEqual(shipping_quote(1.5, "regional", service="express"), 17.25)

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(2, "local", service="overnight")

    def test_unknown_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(2, "international", service="express")
