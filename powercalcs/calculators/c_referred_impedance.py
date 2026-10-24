"""Refer transformer impedance. See docs/calculators/referred_impedance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(resistance, reactance, ratio):
    return dict(referred=complex(resistance,reactance)*ratio**2)

CALCULATOR = Calculator(
    id='referred_impedance', title='Refer transformer impedance', category='Transformers',
    description='Z_target = Z_source (V_target / V_source)². Ideal transformer winding voltage ratio; use winding phase voltage ratio for differing star/delta connections.',
    fields=(
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('reactance', 'Reactance (+ inductive)', 'ohm', 'impedance', 1, None, None, False, False),
    Field('ratio', 'Target/source winding voltage ratio', 'pu', 'ratio', 10, 0, None, True, False),
    ),
    outputs={'referred': 'ohm'},
    formulas=('Z_target = Z_source (V_target / V_source)²',),
    assumptions=('Ideal transformer winding voltage ratio; use winding phase voltage ratio for differing star/delta connections.',),
    compute=compute,
)
