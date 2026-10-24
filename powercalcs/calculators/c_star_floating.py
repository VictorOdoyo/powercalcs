"""Unbalanced star with floating neutral. See docs/calculators/star_floating.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, ra, xa, rb, xb, rc, xc):
    va,vb,vc=phases(voltage)
    ya=1/nonzero(complex(ra,xa));yb=1/nonzero(complex(rb,xb));yc=1/nonzero(complex(rc,xc))
    vn=(va*ya+vb*yb+vc*yc)/nonzero(ya+yb+yc,"Admittance sum")
    ia=(va-vn)*ya;ib=(vb-vn)*yb;ic=(vc-vn)*yc
    s=(va-vn)*ia.conjugate()+(vb-vn)*ib.conjugate()+(vc-vn)*ic.conjugate()
    return dict(neutral_displacement=vn,ia=ia,ib=ib,ic=ic,power=s.real)

CALCULATOR = Calculator(
    id='star_floating', title='Unbalanced star with floating neutral', category='Three phase',
    description='Y_k = 1 / Z_k. Three-wire star load with no neutral connection. Ideal balanced ABC source; no earth shunts.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('ra', 'Phase A resistance', 'ohm', 'impedance', 10, 0, None, False, False),
    Field('xa', 'Phase A reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('rb', 'Phase B resistance', 'ohm', 'impedance', 20, 0, None, False, False),
    Field('xb', 'Phase B reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('rc', 'Phase C resistance', 'ohm', 'impedance', 20, 0, None, False, False),
    Field('xc', 'Phase C reactance', 'ohm', 'impedance', 0, None, None, False, False),
    ),
    outputs={'neutral_displacement': 'V', 'ia': 'A', 'ib': 'A', 'ic': 'A', 'power': 'W'},
    formulas=('Y_k = 1 / Z_k', 'V_n = sum(V_k Y_k) / sum(Y_k)', 'I_k = (V_k - V_n) Y_k', 'P = real(sum((V_k - V_n) conjugate(I_k)))'),
    assumptions=('Three-wire star load with no neutral connection. Ideal balanced ABC source; no earth shunts.',),
    compute=compute,
)
