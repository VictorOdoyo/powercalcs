"""Reconstruct phase phasors. See docs/calculators/sequence_reconstruction.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(zero_mag, zero_angle, positive_mag, positive_angle, negative_mag, negative_angle):
    va,vb,vc=reconstruct(rect(zero_mag,zero_angle),rect(positive_mag,positive_angle),rect(negative_mag,negative_angle))
    return dict(va=va,vb=vb,vc=vc)

CALCULATOR = Calculator(
    id='sequence_reconstruction', title='Reconstruct phase phasors', category='Phasors',
    description='VA = V0 + V1 + V2. ABC positive sequence; a = exp(j 120 degrees).',
    fields=(
    Field('zero_mag', 'zero magnitude', 'V', 'voltage', 10, 0, None, False, False),
    Field('zero_angle', 'zero angle', 'deg', 'angle', 0, None, None, False, False),
    Field('positive_mag', 'positive magnitude', 'V', 'voltage', 230, 0, None, False, False),
    Field('positive_angle', 'positive angle', 'deg', 'angle', 0, None, None, False, False),
    Field('negative_mag', 'negative magnitude', 'V', 'voltage', 0, 0, None, False, False),
    Field('negative_angle', 'negative angle', 'deg', 'angle', 0, None, None, False, False),
    ),
    outputs={'va': 'V', 'vb': 'V', 'vc': 'V'},
    formulas=('VA = V0 + V1 + V2', 'VB = V0 + a² V1 + a V2', 'VC = V0 + a V1 + a² V2'),
    assumptions=('ABC positive sequence; a = exp(j 120 degrees).',),
    compute=compute,
)
