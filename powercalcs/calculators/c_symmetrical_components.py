"""Symmetrical components. See docs/calculators/symmetrical_components.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(a_mag, a_angle, b_mag, b_angle, c_mag, c_angle):
    z,p,n=sequences(rect(a_mag,a_angle),rect(b_mag,b_angle),rect(c_mag,c_angle))
    return dict(zero=z,positive=p,negative=n)

CALCULATOR = Calculator(
    id='symmetrical_components', title='Symmetrical components', category='Phasors',
    description='a = exp(j 120 degrees). ABC positive sequence; RMS voltage phasors use exp(j omega t). Input angles may be degrees or radians.',
    fields=(
    Field('a_mag', 'A magnitude', 'V', 'voltage', 230, 0, None, False, False),
    Field('a_angle', 'A angle', 'deg', 'angle', 0, None, None, False, False),
    Field('b_mag', 'B magnitude', 'V', 'voltage', 230, 0, None, False, False),
    Field('b_angle', 'B angle', 'deg', 'angle', -120, None, None, False, False),
    Field('c_mag', 'C magnitude', 'V', 'voltage', 230, 0, None, False, False),
    Field('c_angle', 'C angle', 'deg', 'angle', 120, None, None, False, False),
    ),
    outputs={'zero': 'V', 'positive': 'V', 'negative': 'V'},
    formulas=('a = exp(j 120 degrees)', 'V0 = (VA + VB + VC) / 3', 'V1 = (VA + a VB + a² VC) / 3', 'V2 = (VA + a² VB + a VC) / 3'),
    assumptions=('ABC positive sequence; RMS voltage phasors use exp(j omega t). Input angles may be degrees or radians.',),
    compute=compute,
)
