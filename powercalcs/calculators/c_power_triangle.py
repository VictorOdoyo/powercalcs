"""Power triangle. See docs/calculators/power_triangle.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, reactive):
    s=hypot(power,reactive)
    nonzero(s,"Apparent power")
    return dict(apparent=s,pf=power/s,angle=degrees(atan2(reactive,power)))

CALCULATOR = Calculator(
    id='power_triangle', title='Power triangle', category='Power',
    description='S = sqrt(P² + Q²). Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('reactive', 'Signed reactive power', 'var', 'reactive_power', 7500, None, None, False, False),
    ),
    outputs={'apparent': 'VA', 'pf': 'pu', 'angle': 'deg'},
    formulas=('S = sqrt(P² + Q²)', 'pf = P / S', 'phi = atan2(Q, P)'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
