"""Series impedance. See docs/calculators/series_impedance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(resistance, reactance):
    z=complex(resistance,reactance)
    return dict(impedance=z,magnitude=abs(z),angle=degrees(atan2(reactance,resistance)))

CALCULATOR = Calculator(
    id='series_impedance', title='Series impedance', category='Impedance',
    description='Z = R + jX. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('reactance', 'Reactance (+ inductive)', 'ohm', 'impedance', 1, None, None, False, False),
    ),
    outputs={'impedance': 'ohm', 'magnitude': 'ohm', 'angle': 'deg'},
    formulas=('Z = R + jX', '|Z| = sqrt(R² + X²)', 'angle(Z) = atan2(X,R)'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
