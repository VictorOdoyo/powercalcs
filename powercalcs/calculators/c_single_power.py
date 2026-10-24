"""Single-phase power. See docs/calculators/single_power.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, current, pf):
    s=voltage*current
    return dict(apparent=s,active=s*pf,reactive=s*sqrt(1-pf*pf))

CALCULATOR = Calculator(
    id='single_power', title='Single-phase power', category='Power',
    description='S = V I. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('voltage', 'RMS voltage', 'V', 'voltage', 230, 0, None, True, False),
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('pf', 'Displacement power factor (lagging)', 'pu', 'ratio', 0.8, 0, 1, False, False),
    ),
    outputs={'apparent': 'VA', 'active': 'W', 'reactive': 'var'},
    formulas=('S = V I', 'P = S pf', 'Q = S sqrt(1 - pf²)'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
