"""Delta capacitor-bank sizing. See docs/calculators/delta_capacitance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, frequency, rating):
    return dict(capacitance_per_phase=rating/(3*2*pi*frequency*voltage**2))

CALCULATOR = Calculator(
    id='delta_capacitance', title='Delta capacitor-bank sizing', category='Capacitors',
    description='C_per_phase = Q_bank / (3 omega V_LL²). Balanced ideal three-phase bank. Output is the capacitance of each star leg or delta branch, not the total capacitance.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('frequency', 'Frequency', 'Hz', 'frequency', 50, 0, None, True, False),
    Field('rating', 'Total bank reactive rating', 'var', 'reactive_power', 50000, 0, None, False, False),
    ),
    outputs={'capacitance_per_phase': 'F'},
    formulas=('C_per_phase = Q_bank / (3 omega V_LL²)', 'omega = 2 pi f'),
    assumptions=('Balanced ideal three-phase bank. Output is the capacitance of each star leg or delta branch, not the total capacitance.',),
    compute=compute,
)
