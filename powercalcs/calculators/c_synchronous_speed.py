"""Motor synchronous speed. See docs/calculators/synchronous_speed.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(frequency, poles):
    if int(poles)%2: raise ValueError("Pole count must be even")
    return dict(speed=120*frequency/poles)

CALCULATOR = Calculator(
    id='synchronous_speed', title='Motor synchronous speed', category='Motors',
    description='n_sync (rpm) = 120 f / poles. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('frequency', 'Frequency', 'Hz', 'frequency', 50, 0, None, True, False),
    Field('poles', 'Pole count', 'count', 'count', 4, 2, None, False, True),
    ),
    outputs={'speed': 'rpm'},
    formulas=('n_sync (rpm) = 120 f / poles',),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
