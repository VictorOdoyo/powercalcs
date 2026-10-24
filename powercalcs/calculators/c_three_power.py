"""Three-phase power. See docs/calculators/three_power.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, current, pf):
    s=sqrt(3)*voltage*current
    return dict(apparent=s,active=s*pf,reactive=s*sqrt(1-pf*pf))

CALCULATOR = Calculator(
    id='three_power', title='Three-phase power', category='Power',
    description='S = sqrt(3) V_LL I_L. Balanced three-phase sinusoidal load. Voltage is line-to-line; current is line current. Lagging power factor.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('pf', 'Displacement power factor (lagging)', 'pu', 'ratio', 0.8, 0, 1, False, False),
    ),
    outputs={'apparent': 'VA', 'active': 'W', 'reactive': 'var'},
    formulas=('S = sqrt(3) V_LL I_L', 'P = S pf', 'Q = S sqrt(1 - pf²)'),
    assumptions=('Balanced three-phase sinusoidal load. Voltage is line-to-line; current is line current. Lagging power factor.',),
    compute=compute,
)
