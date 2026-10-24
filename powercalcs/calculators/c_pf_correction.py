"""Power-factor correction rating. See docs/calculators/pf_correction.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, initial_pf, target_pf):
    if target_pf<initial_pf: raise ValueError("Target power factor must not be lower than initial")
    q1=power*tan(acos(initial_pf));q2=power*tan(acos(target_pf))
    return dict(required_var=q1-q2,initial_var=q1,target_var=q2)

CALCULATOR = Calculator(
    id='pf_correction', title='Power-factor correction rating', category='Capacitors',
    description='Q_initial = P tan(acos(pf_initial)). Sinusoidal lagging load with constant active power. Correction to a lagging target only; harmonic resonance and switching duties require a separate study.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('initial_pf', 'Initial lagging power factor', 'pu', 'ratio', 0.8, 0, 1, True, False),
    Field('target_pf', 'Target lagging power factor', 'pu', 'ratio', 0.95, 0, 1, True, False),
    ),
    outputs={'required_var': 'var', 'initial_var': 'var', 'target_var': 'var'},
    formulas=('Q_initial = P tan(acos(pf_initial))', 'Q_target = P tan(acos(pf_target))', 'Q_capacitor = Q_initial - Q_target'),
    assumptions=('Sinusoidal lagging load with constant active power. Correction to a lagging target only; harmonic resonance and switching duties require a separate study.',),
    compute=compute,
)
