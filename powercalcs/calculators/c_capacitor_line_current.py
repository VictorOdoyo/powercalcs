"""Three-phase capacitor line current. See docs/calculators/capacitor_line_current.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, rating):
    return dict(line_current=rating/(sqrt(3)*voltage))

CALCULATOR = Calculator(
    id='capacitor_line_current', title='Three-phase capacitor line current', category='Capacitors',
    description='I_line = Q_bank / (sqrt(3) V_LL). Balanced sinusoidal ideal capacitor bank. Excludes harmonic current and manufacturing tolerance.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('rating', 'Total bank reactive power', 'var', 'reactive_power', 50000, 0, None, False, False),
    ),
    outputs={'line_current': 'A'},
    formulas=('I_line = Q_bank / (sqrt(3) V_LL)',),
    assumptions=('Balanced sinusoidal ideal capacitor bank. Excludes harmonic current and manufacturing tolerance.',),
    compute=compute,
)
