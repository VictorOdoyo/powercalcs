"""Conductor I²R losses. See docs/calculators/conductor_losses.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(current, resistance, conductors):
    return dict(loss=conductors*current*current*resistance)

CALCULATOR = Calculator(
    id='conductor_losses', title='Conductor I²R losses', category='Cables',
    description='P_loss = n I² R. Equal RMS current and end-to-end resistance in every counted conductor. Neutral losses must be evaluated separately if unequal.',
    fields=(
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('conductors', 'Loaded conductor count', 'count', 'count', 3, 1, None, False, True),
    ),
    outputs={'loss': 'W'},
    formulas=('P_loss = n I² R',),
    assumptions=('Equal RMS current and end-to-end resistance in every counted conductor. Neutral losses must be evaluated separately if unequal.',),
    compute=compute,
)
