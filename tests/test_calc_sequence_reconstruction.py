import unittest
from powercalcs.catalog import calculate

class ReferenceCase(unittest.TestCase):
    def test_worked_reference(self):
        result=calculate('sequence_reconstruction', {'zero_mag': 10, 'zero_angle': 0, 'positive_mag': 230, 'positive_angle': 0, 'negative_mag': 0, 'negative_angle': 0})
        for key, expected in {'va': [240, 0], 'vb': [-105, -199.18584287042088], 'vc': [-105, 199.18584287042088]}.items():
            with self.subTest(output=key):
                actual=result['results'][key]
                if isinstance(expected, list):
                    self.assertAlmostEqual(actual['real'], expected[0], delta=max(1e-8,abs(expected[0])*1e-9))
                    self.assertAlmostEqual(actual['imag'], expected[1], delta=max(1e-8,abs(expected[1])*1e-9))
                else:
                    self.assertAlmostEqual(actual, expected, delta=max(1e-8,abs(expected)*1e-9))
        self.assertTrue(result['steps'])
        self.assertTrue(result['assumptions'])

    def test_missing_input_rejected(self):
        with self.assertRaisesRegex(ValueError, 'Missing inputs'):
            calculate('sequence_reconstruction', {})
