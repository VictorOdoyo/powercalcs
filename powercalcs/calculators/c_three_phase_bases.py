"""Three-phase per-unit bases. See docs/calculators/three_phase_bases.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, apparent):
    return dict(base_current=apparent/(sqrt(3)*voltage),base_impedance=voltage**2/apparent,phase_voltage=voltage/sqrt(3))

CALCULATOR = Calculator(
    id='three_phase_bases', title='Three-phase per-unit bases', category='Transformers',
    description='I_base = S_3phase / (sqrt(3) V_LL). Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('apparent', 'Three-phase base power', 'VA', 'apparent_power', 100000, 0, None, True, False),
    ),
    outputs={'base_current': 'A', 'base_impedance': 'ohm', 'phase_voltage': 'V'},
    formulas=('I_base = S_3phase / (sqrt(3) V_LL)', 'Z_base = V_LL² / S_3phase', 'V_phase_base = V_LL / sqrt(3)'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
