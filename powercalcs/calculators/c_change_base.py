"""Change per-unit impedance base. See docs/calculators/change_base.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(impedance, old_power, new_power, old_voltage, new_voltage):
    return dict(new_impedance=impedance*(new_power/old_power)*(old_voltage/new_voltage)**2)

CALCULATOR = Calculator(
    id='change_base', title='Change per-unit impedance base', category='Transformers',
    description='Z_pu,new = Z_pu,old (S_new/S_old) (V_old/V_new)². Same physical impedance and winding side. Magnitude-only conversion; impedance angle remains unchanged.',
    fields=(
    Field('impedance', 'Impedance magnitude on old base', 'pu', 'ratio', 0.1, 0, None, False, False),
    Field('old_power', 'Old base apparent power', 'VA', 'apparent_power', 1000000.0, 0, None, True, False),
    Field('new_power', 'New base apparent power', 'VA', 'apparent_power', 2000000.0, 0, None, True, False),
    Field('old_voltage', 'Old line voltage base', 'V', 'voltage', 11000, 0, None, True, False),
    Field('new_voltage', 'New line voltage base', 'V', 'voltage', 11000, 0, None, True, False),
    ),
    outputs={'new_impedance': 'pu'},
    formulas=('Z_pu,new = Z_pu,old (S_new/S_old) (V_old/V_new)²',),
    assumptions=('Same physical impedance and winding side. Magnitude-only conversion; impedance angle remains unchanged.',),
    compute=compute,
)
