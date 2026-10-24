"""Two parallel feeder current sharing. See docs/calculators/parallel_feeders.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(current, r1, x1, r2, x2):
    z1=nonzero(complex(r1,x1));z2=nonzero(complex(r2,x2));total=nonzero(z1+z2,"Impedance sum")
    i1=current*z2/total;i2=current*z1/total
    return dict(i1=i1,i2=i2,loss=abs(i1)**2*r1+abs(i2)**2*r2)

CALCULATOR = Calculator(
    id='parallel_feeders', title='Two parallel feeder current sharing', category='Cables',
    description='I1 = I_total Z2 / (Z1 + Z2). Two uncoupled branches with common terminals; total current is the zero-angle reference phasor. Mutual impedance omitted.',
    fields=(
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('r1', 'Feeder 1 resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('x1', 'Feeder 1 reactance', 'ohm', 'impedance', 0, None, None, False, False),
    Field('r2', 'Feeder 2 resistance', 'ohm', 'impedance', 2, 0, None, False, False),
    Field('x2', 'Feeder 2 reactance', 'ohm', 'impedance', 0, None, None, False, False),
    ),
    outputs={'i1': 'A', 'i2': 'A', 'loss': 'W'},
    formulas=('I1 = I_total Z2 / (Z1 + Z2)', 'I2 = I_total Z1 / (Z1 + Z2)', 'P_loss = |I1|² R1 + |I2|² R2'),
    assumptions=('Two uncoupled branches with common terminals; total current is the zero-angle reference phasor. Mutual impedance omitted.',),
    compute=compute,
)
