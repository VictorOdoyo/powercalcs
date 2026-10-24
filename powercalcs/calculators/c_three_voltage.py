"""Three-phase voltage. See docs/calculators/three_voltage.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, current, pf):
    return dict(voltage=power/(sqrt(3)*current*pf))

CALCULATOR = Calculator(
    id='three_voltage', title='Three-phase voltage', category='Power',
    description='V = P / (sqrt(3) I pf). Total active electrical power; three-phase output is balanced line-to-line voltage.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('current', 'RMS current', 'A', 'current', 10, 0, None, True, False),
    Field('pf', 'Power factor', 'pu', 'ratio', 0.8, 0, 1, True, False),
    ),
    outputs={'voltage': 'V'},
    formulas=('V = P / (sqrt(3) I pf)',),
    assumptions=('Total active electrical power; three-phase output is balanced line-to-line voltage.',),
    compute=compute,
)
