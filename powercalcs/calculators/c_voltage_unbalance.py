"""Sequence voltage unbalance. See docs/calculators/voltage_unbalance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(positive, negative):
    return dict(unbalance_percent=100*negative/positive)

CALCULATOR = Calculator(
    id='voltage_unbalance', title='Sequence voltage unbalance', category='Phasors',
    description='VUF (%) = 100 |V2| / |V1|. Sequence-based voltage unbalance factor; input sequence magnitudes must come from a consistent phasor measurement.',
    fields=(
    Field('positive', 'Positive-sequence magnitude', 'V', 'voltage', 230, 0, None, True, False),
    Field('negative', 'Negative-sequence magnitude', 'V', 'voltage', 4.6, 0, None, False, False),
    ),
    outputs={'unbalance_percent': '%'},
    formulas=('VUF (%) = 100 |V2| / |V1|',),
    assumptions=('Sequence-based voltage unbalance factor; input sequence magnitudes must come from a consistent phasor measurement.',),
    compute=compute,
)
