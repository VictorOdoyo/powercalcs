"""Induction motor slip. See docs/calculators/motor_slip.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(sync_speed, rotor_speed, frequency):
    s=(sync_speed-rotor_speed)/sync_speed
    return dict(slip=s,slip_percent=100*s,rotor_frequency=abs(s)*frequency)

CALCULATOR = Calculator(
    id='motor_slip', title='Induction motor slip', category='Motors',
    description='s = (n_sync - n_rotor) / n_sync. Signed slip permits generating operation when rotor speed exceeds synchronous speed; rotor frequency is a magnitude.',
    fields=(
    Field('sync_speed', 'Synchronous speed', 'rpm', 'speed', 1500, 0, None, True, False),
    Field('rotor_speed', 'Rotor mechanical speed', 'rpm', 'speed', 1440, 0, None, False, False),
    Field('frequency', 'Frequency', 'Hz', 'frequency', 50, 0, None, True, False),
    ),
    outputs={'slip': 'pu', 'slip_percent': '%', 'rotor_frequency': 'Hz'},
    formulas=('s = (n_sync - n_rotor) / n_sync', 'slip (%) = 100 s', 'f_rotor = |s| f_supply'),
    assumptions=('Signed slip permits generating operation when rotor speed exceeds synchronous speed; rotor frequency is a magnitude.',),
    compute=compute,
)
