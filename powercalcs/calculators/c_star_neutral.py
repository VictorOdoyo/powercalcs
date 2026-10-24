"""Unbalanced star with neutral. See docs/calculators/star_neutral.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, ra, xa, rb, xb, rc, xc):
    va,vb,vc=phases(voltage)
    ia=va/nonzero(complex(ra,xa));ib=vb/nonzero(complex(rb,xb));ic=vc/nonzero(complex(rc,xc))
    s=va*ia.conjugate()+vb*ib.conjugate()+vc*ic.conjugate()
    return dict(ia=ia,ib=ib,ic=ic,neutral_return=ia+ib+ic,power=s.real,reactive=s.imag)

CALCULATOR = Calculator(
    id='star_neutral', title='Unbalanced star with neutral', category='Three phase',
    description='V_A,V_B,V_C = (V_LL/sqrt(3)) at 0,-120,+120 degrees. Ideal zero-impedance neutral fixes the load star point. Phase currents flow source to load; neutral return flows load to source.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('ra', 'Phase A resistance', 'ohm', 'impedance', 10, 0, None, False, False),
    Field('xa', 'Phase A reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('rb', 'Phase B resistance', 'ohm', 'impedance', 20, 0, None, False, False),
    Field('xb', 'Phase B reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('rc', 'Phase C resistance', 'ohm', 'impedance', 20, 0, None, False, False),
    Field('xc', 'Phase C reactance', 'ohm', 'impedance', 0, None, None, False, False),
    ),
    outputs={'ia': 'A', 'ib': 'A', 'ic': 'A', 'neutral_return': 'A', 'power': 'W', 'reactive': 'var'},
    formulas=('V_A,V_B,V_C = (V_LL/sqrt(3)) at 0,-120,+120 degrees', 'I_k = V_k / Z_k', 'I_neutral_return = I_A + I_B + I_C', 'S_total = sum(V_k conjugate(I_k))'),
    assumptions=('Ideal zero-impedance neutral fixes the load star point. Phase currents flow source to load; neutral return flows load to source.',),
    compute=compute,
)
