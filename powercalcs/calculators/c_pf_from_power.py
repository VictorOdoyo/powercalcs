"""Power factor from P and S. See docs/calculators/pf_from_power.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, apparent):
    if power>apparent: raise ValueError("Active power cannot exceed apparent power")
    return dict(pf=power/apparent,reactive=sqrt(apparent**2-power**2))

CALCULATOR = Calculator(
    id='pf_from_power', title='Power factor from P and S', category='Power',
    description='pf = P / S. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('apparent', 'Apparent power', 'VA', 'apparent_power', 12500, 0, None, True, False),
    ),
    outputs={'pf': 'pu', 'reactive': 'var'},
    formulas=('pf = P / S', 'Q = sqrt(S² - P²)'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
