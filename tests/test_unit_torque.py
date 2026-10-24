import unittest
from powercalcs.units import convert

class UnitTests(unittest.TestCase):
    def test_conversion(self):
        for unit, scale in {'Nm': 1, 'kNm': 1000}.items():
            with self.subTest(unit=unit):
                self.assertAlmostEqual(convert(2.5, unit, 'torque'), 2.5 * scale)

    def test_dimension_rejection(self):
        with self.assertRaises(ValueError):
            convert(1, 'Nm', 'invalid-dimension')
