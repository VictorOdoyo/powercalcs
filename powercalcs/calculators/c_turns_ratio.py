"""Ideal transformer turns ratio. See docs/calculators/turns_ratio.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(primary, secondary, secondary_current):
    a=primary/secondary
    return dict(ratio=a,primary_current=secondary_current/a)

CALCULATOR = Calculator(
    id='turns_ratio', title='Ideal transformer turns ratio', category='Transformers',
    description='a = V_primary / V_secondary = N_primary / N_secondary. Ideal transformer; voltages and currents are winding quantities, not necessarily line quantities.',
    fields=(
    Field('primary', 'Primary winding RMS voltage', 'V', 'voltage', 11000, 0, None, True, False),
    Field('secondary', 'Secondary winding RMS voltage', 'V', 'voltage', 230, 0, None, True, False),
    Field('secondary_current', 'Secondary winding current', 'A', 'current', 100, 0, None, False, False),
    ),
    outputs={'ratio': 'pu', 'primary_current': 'A'},
    formulas=('a = V_primary / V_secondary = N_primary / N_secondary', 'I_primary = I_secondary / a'),
    assumptions=('Ideal transformer; voltages and currents are winding quantities, not necessarily line quantities.',),
    compute=compute,
)
