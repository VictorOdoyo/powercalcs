"""Approximate transformer regulation. See docs/calculators/transformer_regulation.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(resistance_pu, reactance_pu, pf, loading):
    return dict(regulation_percent=100*loading*(resistance_pu*pf+reactance_pu*sqrt(1-pf*pf)))

CALCULATOR = Calculator(
    id='transformer_regulation', title='Approximate transformer regulation', category='Transformers',
    description='regulation (%) approximately 100 loading (R_pu pf + X_pu sin(phi)). First-order lagging-load regulation estimate on a consistent transformer base. Magnetizing branch omitted.',
    fields=(
    Field('resistance_pu', 'Resistance', 'pu', 'ratio', 0.01, 0, None, False, False),
    Field('reactance_pu', 'Reactance', 'pu', 'ratio', 0.04, None, None, False, False),
    Field('pf', 'Displacement power factor (lagging)', 'pu', 'ratio', 0.8, 0, 1, False, False),
    Field('loading', 'Load fraction', 'pu', 'ratio', 1, 0, None, False, False),
    ),
    outputs={'regulation_percent': '%'},
    formulas=('regulation (%) approximately 100 loading (R_pu pf + X_pu sin(phi))',),
    assumptions=('First-order lagging-load regulation estimate on a consistent transformer base. Magnetizing branch omitted.',),
    compute=compute,
)
