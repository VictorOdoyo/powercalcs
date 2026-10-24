"""Resistance at temperature. See docs/calculators/temperature_resistance.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(resistance, alpha, reference_temp, temperature):
    factor=1+alpha*(temperature-reference_temp)
    if factor<=0: raise ValueError("Temperature model gives nonpositive resistance factor")
    return dict(resistance_hot=resistance*factor)

CALCULATOR = Calculator(
    id='temperature_resistance', title='Resistance at temperature', category='Cables',
    description='R(T) = R_ref [1 + alpha_ref (T - T_ref)]. Linear resistance-temperature approximation; alpha is referenced to T_ref. No thermal equilibrium calculation.',
    fields=(
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('alpha', 'Temperature coefficient at reference', '1/degC', 'temperature_coefficient', 0.00393, 0, None, False, False),
    Field('reference_temp', 'Reference temperature', 'degC', 'temperature', 20, None, None, False, False),
    Field('temperature', 'Operating temperature', 'degC', 'temperature', 70, None, None, False, False),
    ),
    outputs={'resistance_hot': 'ohm'},
    formulas=('R(T) = R_ref [1 + alpha_ref (T - T_ref)]',),
    assumptions=('Linear resistance-temperature approximation; alpha is referenced to T_ref. No thermal equilibrium calculation.',),
    compute=compute,
)
