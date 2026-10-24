import unittest
from powercalcs.units import convert

class UnitTests(unittest.TestCase):
    def test_conversion(self):
        for unit, scale in {'pu': 1, '%': 0.01}.items():
            with self.subTest(unit=unit):
                self.assertAlmostEqual(convert(2.5, unit, 'ratio'), 2.5 * scale)

    def test_dimension_rejection(self):
        with self.assertRaises(ValueError):
            convert(1, 'pu', 'invalid-dimension')
