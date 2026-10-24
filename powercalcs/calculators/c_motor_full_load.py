"""Motor full-load electrical current. See docs/calculators/motor_full_load.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(shaft_power, voltage, efficiency, pf):
    p=shaft_power/efficiency
    return dict(input_power=p,current=p/(sqrt(3)*voltage*pf),losses=p-shaft_power)

CALCULATOR = Calculator(
    id='motor_full_load', title='Motor full-load electrical current', category='Motors',
    description='P_input = P_shaft / eta. Balanced three-phase motor at the specified operating efficiency and displacement power factor.',
    fields=(
    Field('shaft_power', 'Mechanical shaft output', 'W', 'power', 15000, 0, None, False, False),
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('efficiency', 'Efficiency', 'pu', 'ratio', 0.9, 0, 1, True, False),
    Field('pf', 'Power factor', 'pu', 'ratio', 0.85, 0, 1, True, False),
    ),
    outputs={'input_power': 'W', 'current': 'A', 'losses': 'W'},
    formulas=('P_input = P_shaft / eta', 'I_L = P_input / (sqrt(3) V_LL pf)', 'P_loss = P_input - P_shaft'),
    assumptions=('Balanced three-phase motor at the specified operating efficiency and displacement power factor.',),
    compute=compute,
)
