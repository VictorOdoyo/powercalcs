"""Parallel complex impedances. See docs/calculators/parallel_impedance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(r1, x1, r2, x2):
    z1=nonzero(complex(r1,x1));z2=nonzero(complex(r2,x2))
    return dict(equivalent=z1*z2/nonzero(z1+z2,"Impedance sum"))

CALCULATOR = Calculator(
    id='parallel_impedance', title='Parallel complex impedances', category='Impedance',
    description='Z_eq = Z1 Z2 / (Z1 + Z2). Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('r1', 'Branch 1 resistance', 'ohm', 'impedance', 10, 0, None, False, False),
    Field('x1', 'Branch 1 reactance', 'ohm', 'impedance', 10, None, None, False, False),
    Field('r2', 'Branch 2 resistance', 'ohm', 'impedance', 10, 0, None, False, False),
    Field('x2', 'Branch 2 reactance', 'ohm', 'impedance', 10, None, None, False, False),
    ),
    outputs={'equivalent': 'ohm'},
    formulas=('Z_eq = Z1 Z2 / (Z1 + Z2)',),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
