"""Load energy and utilization. See docs/calculators/energy_consumption.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(power, duration, utilization):
    e=power*duration*utilization
    return dict(energy=e,energy_kwh=e/3.6e6,average_power=power*utilization)

CALCULATOR = Calculator(
    id='energy_consumption', title='Load energy and utilization', category='Studies',
    description='P_average = P_rated utilization. Constant average utilization over the specified duration; no tariff or demand-charge model.',
    fields=(
    Field('power', 'Active power', 'W', 'power', 10000, 0, None, False, False),
    Field('duration', 'Duration', 's', 'time', 3600, 0, None, False, False),
    Field('utilization', 'Average utilization', 'pu', 'ratio', 0.75, 0, 1, False, False),
    ),
    outputs={'energy': 'J', 'energy_kwh': 'kWh', 'average_power': 'W'},
    formulas=('P_average = P_rated utilization', 'E = P_average duration', 'E_kWh = E_J / 3.6e6'),
    assumptions=('Constant average utilization over the specified duration; no tariff or demand-charge model.',),
    compute=compute,
)
