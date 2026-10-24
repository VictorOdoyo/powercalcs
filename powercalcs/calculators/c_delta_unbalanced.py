"""Unbalanced delta currents. See docs/calculators/delta_unbalanced.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, ra, xa, rb, xb, rc, xc):
    va,vb,vc=phases(voltage)
    iab=(va-vb)/nonzero(complex(ra,xa));ibc=(vb-vc)/nonzero(complex(rb,xb));ica=(vc-va)/nonzero(complex(rc,xc))
    s=(va-vb)*iab.conjugate()+(vb-vc)*ibc.conjugate()+(vc-va)*ica.conjugate()
    return dict(iab=iab,ibc=ibc,ica=ica,ia=iab-ica,ib=ibc-iab,ic=ica-ibc,power=s.real)

CALCULATOR = Calculator(
    id='delta_unbalanced', title='Unbalanced delta currents', category='Three phase',
    description='I_AB = (V_A - V_B) / Z_AB; similarly BC and CA. Inputs labelled phase A/B/C represent delta branches AB/BC/CA respectively. Branch directions AB, BC, CA; ideal ABC source.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('ra', 'Phase A resistance', 'ohm', 'impedance', 10, 0, None, False, False),
    Field('xa', 'Phase A reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('rb', 'Phase B resistance', 'ohm', 'impedance', 20, 0, None, False, False),
    Field('xb', 'Phase B reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('rc', 'Phase C resistance', 'ohm', 'impedance', 20, 0, None, False, False),
    Field('xc', 'Phase C reactance', 'ohm', 'impedance', 0, None, None, False, False),
    ),
    outputs={'iab': 'A', 'ibc': 'A', 'ica': 'A', 'ia': 'A', 'ib': 'A', 'ic': 'A', 'power': 'W'},
    formulas=('I_AB = (V_A - V_B) / Z_AB; similarly BC and CA', 'I_A = I_AB - I_CA; I_B = I_BC - I_AB; I_C = I_CA - I_BC', 'P = real(sum(V_branch conjugate(I_branch)))'),
    assumptions=('Inputs labelled phase A/B/C represent delta branches AB/BC/CA respectively. Branch directions AB, BC, CA; ideal ABC source.',),
    compute=compute,
)
