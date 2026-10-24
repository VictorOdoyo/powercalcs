"""Single-phase feeder voltage drop. See docs/calculators/single_voltage_drop.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, current, resistance, reactance, length, pf):
    drop=2*current*length*(resistance*pf+reactance*sqrt(1-pf*pf))
    return dict(drop=drop,percent=100*drop/voltage,receiving_approx=voltage-drop)

CALCULATOR = Calculator(
    id='single_voltage_drop', title='Single-phase feeder voltage drop', category='Cables',
    description='dV = 2 I L (R pf + X sqrt(1-pf²)). First-order longitudinal drop approximation, sinusoidal lagging load. R and X are per conductor per metre; length is one-way. Three-phase case is balanced; single-phase has identical outgoing and return conductors.',
    fields=(
    Field('voltage', 'RMS voltage', 'V', 'voltage', 230, 0, None, True, False),
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('resistance', 'Per-conductor resistance per metre', 'ohm/m', 'impedance_per_length', 0.0005, 0, None, False, False),
    Field('reactance', 'Per-conductor reactance per metre', 'ohm/m', 'impedance_per_length', 8e-05, None, None, False, False),
    Field('length', 'One-way route length', 'm', 'length', 100, 0, None, False, False),
    Field('pf', 'Displacement power factor (lagging)', 'pu', 'ratio', 0.8, 0, 1, False, False),
    ),
    outputs={'drop': 'V', 'percent': '%', 'receiving_approx': 'V'},
    formulas=('dV = 2 I L (R pf + X sqrt(1-pf²))', 'drop (%) = 100 dV / V', 'V_receiving approximately V - dV'),
    assumptions=('First-order longitudinal drop approximation, sinusoidal lagging load. R and X are per conductor per metre; length is one-way. Three-phase case is balanced; single-phase has identical outgoing and return conductors.',),
    compute=compute,
)
