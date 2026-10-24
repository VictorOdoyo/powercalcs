"""Balanced star load. See docs/calculators/balanced_star.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, resistance, reactance):
    z=nonzero(complex(resistance,reactance))
    v=voltage/sqrt(3);i=v/z;s=3*v*i.conjugate()
    return dict(phase_voltage=v,line_current=abs(i),power=s.real,reactive=s.imag)

CALCULATOR = Calculator(
    id='balanced_star', title='Balanced star load', category='Three phase',
    description='V_phase = V_LL / sqrt(3). Balanced star-connected impedance load; ABC ideal sinusoidal source.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('reactance', 'Reactance (+ inductive)', 'ohm', 'impedance', 1, None, None, False, False),
    ),
    outputs={'phase_voltage': 'V', 'line_current': 'A', 'power': 'W', 'reactive': 'var'},
    formulas=('V_phase = V_LL / sqrt(3)', 'I_L = V_phase / Z', 'S_total = 3 V_phase conjugate(I_L)'),
    assumptions=('Balanced star-connected impedance load; ABC ideal sinusoidal source.',),
    compute=compute,
)
