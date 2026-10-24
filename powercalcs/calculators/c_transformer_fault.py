"""Transformer-limited three-phase fault. See docs/calculators/transformer_fault.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, apparent, impedance_pu):
    rated=apparent/(sqrt(3)*voltage)
    return dict(rated_current=rated,fault_current=rated/impedance_pu)

CALCULATOR = Calculator(
    id='transformer_fault', title='Transformer-limited three-phase fault', category='Transformers',
    description='I_rated = S / (sqrt(3) V_LL). Simplified symmetrical RMS bolted fault estimate with an infinite upstream source. Excludes source/cable impedance, voltage factors, motor contribution, and DC offset; not a standard-compliant fault study.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('apparent', 'Transformer rating', 'VA', 'apparent_power', 100000, 0, None, True, False),
    Field('impedance_pu', 'Transformer impedance magnitude', 'pu', 'ratio', 0.05, 0, None, True, False),
    ),
    outputs={'rated_current': 'A', 'fault_current': 'A'},
    formulas=('I_rated = S / (sqrt(3) V_LL)', 'I_fault approximately I_rated / |Z_pu|'),
    assumptions=('Simplified symmetrical RMS bolted fault estimate with an infinite upstream source. Excludes source/cable impedance, voltage factors, motor contribution, and DC offset; not a standard-compliant fault study.',),
    compute=compute,
)
