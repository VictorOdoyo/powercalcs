"""Motor starting feeder drop. See docs/calculators/motor_start_drop.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, start_current, resistance, reactance, start_pf):
    drop=sqrt(3)*start_current*(resistance*start_pf+reactance*sqrt(1-start_pf**2))
    return dict(drop=drop,drop_percent=100*drop/voltage)

CALCULATOR = Calculator(
    id='motor_start_drop', title='Motor starting feeder drop', category='Motors',
    description='dV approximately sqrt(3) I_start (R pf_start + X sqrt(1-pf_start²)). First-order balanced feeder drop at fixed specified starting current; R/X are total per-phase feeder impedances. Does not solve voltage-dependent motor starting or acceleration.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('start_current', 'Starting RMS current', 'A', 'current', 300, 0, None, False, False),
    Field('resistance', 'Resistance', 'ohm', 'impedance', 1, 0, None, False, False),
    Field('reactance', 'Reactance (+ inductive)', 'ohm', 'impedance', 1, None, None, False, False),
    Field('start_pf', 'Starting lagging power factor', 'pu', 'ratio', 0.35, 0, 1, False, False),
    ),
    outputs={'drop': 'V', 'drop_percent': '%'},
    formulas=('dV approximately sqrt(3) I_start (R pf_start + X sqrt(1-pf_start²))',),
    assumptions=('First-order balanced feeder drop at fixed specified starting current; R/X are total per-phase feeder impedances. Does not solve voltage-dependent motor starting or acceleration.',),
    compute=compute,
)
