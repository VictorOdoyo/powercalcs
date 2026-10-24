import unittest
from powercalcs.units import convert

class UnitTests(unittest.TestCase):
    def test_conversion(self):
        for unit, scale in {'1/degC': 1}.items():
            with self.subTest(unit=unit):
                self.assertAlmostEqual(convert(2.5, unit, 'temperature_coefficient'), 2.5 * scale)

    def test_dimension_rejection(self):
        with self.assertRaises(ValueError):
            convert(1, '1/degC', 'invalid-dimension')
