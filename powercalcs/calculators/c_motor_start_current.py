"""Motor starting current. See docs/calculators/motor_start_current.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(current, multiple):
    return dict(starting_current=current*multiple)

CALCULATOR = Calculator(
    id='motor_start_current', title='Motor starting current', category='Motors',
    description='I_start = multiple I_full_load. Specified starting-current multiple; ignores acceleration, voltage dependence, and starter dynamics.',
    fields=(
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('multiple', 'Locked-rotor current multiple', 'pu', 'ratio', 6, 0, None, False, False),
    ),
    outputs={'starting_current': 'A'},
    formulas=('I_start = multiple I_full_load',),
    assumptions=('Specified starting-current multiple; ignores acceleration, voltage dependence, and starter dynamics.',),
    compute=compute,
)
