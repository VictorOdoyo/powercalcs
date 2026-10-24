import unittest
from powercalcs.units import convert

class UnitTests(unittest.TestCase):
    def test_conversion(self):
        for unit, scale in {'ohm*m': 1, 'ohm*mm2/m': 1e-06}.items():
            with self.subTest(unit=unit):
                self.assertAlmostEqual(convert(2.5, unit, 'resistivity'), 2.5 * scale)

    def test_dimension_rejection(self):
        with self.assertRaises(ValueError):
            convert(1, 'ohm*m', 'invalid-dimension')
