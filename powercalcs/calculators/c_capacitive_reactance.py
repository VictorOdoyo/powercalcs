"""Capacitive reactance. See docs/calculators/capacitive_reactance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(frequency, capacitance):
    return dict(reactance=-1/(2*pi*frequency*capacitance))

CALCULATOR = Calculator(
    id='capacitive_reactance', title='Capacitive reactance', category='Impedance',
    description='X_C = -1 / (2 pi f C). Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('frequency', 'Frequency', 'Hz', 'frequency', 50, 0, None, True, False),
    Field('capacitance', 'Capacitance', 'F', 'capacitance', 0.0001, 0, None, True, False),
    ),
    outputs={'reactance': 'ohm'},
    formulas=('X_C = -1 / (2 pi f C)',),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
