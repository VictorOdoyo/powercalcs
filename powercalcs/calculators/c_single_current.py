"""Single-phase current. See docs/calculators/single_current.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, voltage, pf):
    return dict(current=power/(1*voltage*pf))

CALCULATOR = Calculator(
    id='single_current', title='Single-phase current', category='Power',
    description='I = P / (1 V pf). Sinusoidal load. Three-phase option assumes balance and line-to-line voltage. Active power is total electrical input.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('voltage', 'RMS voltage', 'V', 'voltage', 230, 0, None, True, False),
    Field('pf', 'Displacement power factor', 'pu', 'ratio', 0.8, 0, 1, True, False),
    ),
    outputs={'current': 'A'},
    formulas=('I = P / (1 V pf)',),
    assumptions=('Sinusoidal load. Three-phase option assumes balance and line-to-line voltage. Active power is total electrical input.',),
    compute=compute,
)
