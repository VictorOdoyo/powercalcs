"""Ideal LC resonance. See docs/calculators/resonant_frequency.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(inductance, capacitance):
    return dict(frequency=1/(2*pi*sqrt(inductance*capacitance)))

CALCULATOR = Calculator(
    id='resonant_frequency', title='Ideal LC resonance', category='Impedance',
    description='f0 = 1 / (2 pi sqrt(L C)). Ideal lumped LC circuit; parasitic losses, source impedance, and distributed effects omitted.',
    fields=(
    Field('inductance', 'Inductance', 'H', 'inductance', 0.01, 0, None, True, False),
    Field('capacitance', 'Capacitance', 'F', 'capacitance', 0.0001, 0, None, True, False),
    ),
    outputs={'frequency': 'Hz'},
    formulas=('f0 = 1 / (2 pi sqrt(L C))',),
    assumptions=('Ideal lumped LC circuit; parasitic losses, source impedance, and distributed effects omitted.',),
    compute=compute,
)
