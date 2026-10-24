"""Power-factor phase angle. See docs/calculators/phase_angle.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(pf):
    if pf==0: raise ValueError("tan(phi) is undefined at zero power factor")
    a=acos(pf)
    return dict(angle=degrees(a),tan_phi=tan(a))

CALCULATOR = Calculator(
    id='phase_angle', title='Power-factor phase angle', category='Power',
    description='phi = acos(pf). Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('pf', 'Displacement power factor (lagging)', 'pu', 'ratio', 0.8, 0, 1, False, False),
    ),
    outputs={'angle': 'deg', 'tan_phi': 'pu'},
    formulas=('phi = acos(pf)', 'tan(phi) = sqrt(1 - pf²) / pf'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
