"""Mechanical shaft torque. See docs/calculators/shaft_torque.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, speed):
    omega=2*pi*speed/60
    return dict(torque=power/omega,angular_speed=omega)

CALCULATOR = Calculator(
    id='shaft_torque', title='Mechanical shaft torque', category='Motors',
    description='omega = 2 pi n / 60. Steady mechanical shaft power and nonzero rotational speed; no transient inertial torque.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('speed', 'Shaft speed', 'rpm', 'speed', 1500, 0, None, True, False),
    ),
    outputs={'torque': 'Nm', 'angular_speed': 'rad/s'},
    formulas=('omega = 2 pi n / 60', 'T = P_shaft / omega'),
    assumptions=('Steady mechanical shaft power and nonzero rotational speed; no transient inertial torque.',),
    compute=compute,
)
