import unittest
from powercalcs.units import convert

class UnitTests(unittest.TestCase):
    def test_conversion(self):
        for unit, scale in {'Wb': 1, 'mWb': 0.001}.items():
            with self.subTest(unit=unit):
                self.assertAlmostEqual(convert(2.5, unit, 'flux'), 2.5 * scale)

    def test_dimension_rejection(self):
        with self.assertRaises(ValueError):
            convert(1, 'Wb', 'invalid-dimension')
