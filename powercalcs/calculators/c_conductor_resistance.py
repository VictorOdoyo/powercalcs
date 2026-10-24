"""Resistance from geometry. See docs/calculators/conductor_resistance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(resistivity, length, area):
    return dict(resistance=resistivity*length/area)

CALCULATOR = Calculator(
    id='conductor_resistance', title='Resistance from geometry', category='Cables',
    description='R = rho L / A. Uniform conductor and specified material temperature. DC resistance; skin and proximity effects omitted.',
    fields=(
    Field('resistivity', 'Material resistivity', 'ohm*m', 'resistivity', 1.724e-08, 0, None, True, False),
    Field('length', 'Conductor length', 'm', 'length', 100, 0, None, False, False),
    Field('area', 'Cross-sectional area', 'm2', 'area', 2.5e-05, 0, None, True, False),
    ),
    outputs={'resistance': 'ohm'},
    formulas=('R = rho L / A',),
    assumptions=('Uniform conductor and specified material temperature. DC resistance; skin and proximity effects omitted.',),
    compute=compute,
)
