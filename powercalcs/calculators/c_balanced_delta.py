"""Balanced delta load. See docs/calculators/balanced_delta.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, resistance, reactance):
    z=nonzero(complex(resistance,reactance));i=voltage/z;s=3*voltage*i.conjugate()
    return dict(branch_current=abs(i),line_current=sqrt(3)*abs(i),power=s.real,reactive=s.imag)

CALCULATOR = Calculator(
    id='balanced_delta', title='Balanced delta load', category='Three phase',
    description='V_branch = V_LL. Balanced delta impedance load. Line current magnitude differs from branch current.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('reactance', 'Reactance (+ inductive)', 'ohm', 'impedance', 1, None, None, False, False),
    ),
    outputs={'branch_current': 'A', 'line_current': 'A', 'power': 'W', 'reactive': 'var'},
    formulas=('V_branch = V_LL', 'I_branch = V_LL / Z', '|I_line| = sqrt(3) |I_branch|', 'S_total = 3 V_LL conjugate(I_branch)'),
    assumptions=('Balanced delta impedance load. Line current magnitude differs from branch current.',),
    compute=compute,
)
