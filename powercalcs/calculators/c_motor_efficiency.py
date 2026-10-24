"""Motor efficiency and losses. See docs/calculators/motor_efficiency.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(input_power, output_power):
    if output_power>input_power: raise ValueError("Output cannot exceed input for this motoring model")
    eta=output_power/input_power
    return dict(efficiency=eta,percent=eta*100,losses=input_power-output_power)

CALCULATOR = Calculator(
    id='motor_efficiency', title='Motor efficiency and losses', category='Motors',
    description='eta = P_output / P_input. Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',
    fields=(
    Field('input_power', 'Electrical input power', 'W', 'power', 10000, 0, None, True, False),
    Field('output_power', 'Mechanical output power', 'W', 'power', 9000, 0, None, False, False),
    ),
    outputs={'efficiency': 'pu', 'percent': '%', 'losses': 'W'},
    formulas=('eta = P_output / P_input', 'losses = P_input - P_output'),
    assumptions=('Sinusoidal steady-state RMS quantities. Passive load sign convention; positive Q is inductive.',),
    compute=compute,
)
