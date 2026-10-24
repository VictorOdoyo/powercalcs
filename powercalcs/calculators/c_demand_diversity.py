"""Demand and diversity factors. See docs/calculators/demand_diversity.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(connected, maximum, individual_sum):
    if maximum>connected or maximum>individual_sum or individual_sum>connected: raise ValueError("Require coincident demand <= individual maxima sum <= connected load")
    nonzero(maximum,"Maximum demand")
    return dict(demand_factor=maximum/connected,diversity_factor=individual_sum/maximum,coincidence_factor=maximum/individual_sum)

CALCULATOR = Calculator(
    id='demand_diversity', title='Demand and diversity factors', category='Studies',
    description='Demand factor = coincident maximum / connected load. All demands use the same averaging interval and active-power basis. Connected loads are upper bounds for individual maximum demand.',
    fields=(
    Field('connected', 'Total connected load', 'W', 'power', 100000, 0, None, True, False),
    Field('maximum', 'Coincident maximum demand', 'W', 'power', 60000, 0, None, False, False),
    Field('individual_sum', 'Sum of individual maximum demands', 'W', 'power', 90000, 0, None, True, False),
    ),
    outputs={'demand_factor': 'pu', 'diversity_factor': 'pu', 'coincidence_factor': 'pu'},
    formulas=('Demand factor = coincident maximum / connected load', 'Diversity factor = sum(individual maxima) / coincident maximum', 'Coincidence factor = coincident maximum / sum(individual maxima)'),
    assumptions=('All demands use the same averaging interval and active-power basis. Connected loads are upper bounds for individual maximum demand.',),
    compute=compute,
)
