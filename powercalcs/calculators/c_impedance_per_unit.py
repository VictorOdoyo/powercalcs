"""Impedance to per unit. See docs/calculators/impedance_per_unit.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(resistance, reactance, base_impedance):
    return dict(impedance_pu=complex(resistance,reactance)/base_impedance)

CALCULATOR = Calculator(
    id='impedance_per_unit', title='Impedance to per unit', category='Transformers',
    description='Z_pu = Z_ohm / Z_base. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('reactance', 'Reactance (+ inductive)', 'ohm', 'impedance', 1, None, None, False, False),
    Field('base_impedance', 'Base impedance', 'ohm', 'impedance', 10, 0, None, True, False),
    ),
    outputs={'impedance_pu': 'pu'},
    formulas=('Z_pu = Z_ohm / Z_base',),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
