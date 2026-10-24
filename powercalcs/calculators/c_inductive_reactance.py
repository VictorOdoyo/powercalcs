"""Inductive reactance. See docs/calculators/inductive_reactance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(frequency, inductance):
    return dict(reactance=2*pi*frequency*inductance)

CALCULATOR = Calculator(
    id='inductive_reactance', title='Inductive reactance', category='Impedance',
    description='X_L = 2 pi f L. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('frequency', 'Frequency', 'Hz', 'frequency', 50, 0, None, True, False),
    Field('inductance', 'Inductance', 'H', 'inductance', 0.01, 0, None, False, False),
    ),
    outputs={'reactance': 'ohm'},
    formulas=('X_L = 2 pi f L',),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
