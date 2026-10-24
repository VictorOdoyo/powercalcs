import unittest
from powercalcs.catalog import calculate

class ReferenceCase(unittest.TestCase):
    def test_worked_reference(self):
        result=calculate('motor_start_drop', {'voltage': 400, 'start_current': 300, 'resistance': 1, 'reactance': 1, 'start_pf': 0.35})
        for key, expected in {'drop': 668.6037188883105}.items():
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
            calculate('motor_start_drop', {})
