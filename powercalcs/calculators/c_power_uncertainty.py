"""Three-phase power measurement uncertainty. See docs/calculators/power_uncertainty.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(voltage, current, pf, u_voltage, u_current, u_pf, coverage):
    p=sqrt(3)*voltage*current*pf
    u=sqrt((sqrt(3)*current*pf*u_voltage)**2+(sqrt(3)*voltage*pf*u_current)**2+(sqrt(3)*voltage*current*u_pf)**2)
    e=coverage*u
    return dict(power=p,standard_uncertainty=u,expanded_uncertainty=e,lower=p-e,upper=p+e)

CALCULATOR = Calculator(
    id='power_uncertainty', title='Three-phase power measurement uncertainty', category='Studies',
    description='P = sqrt(3) V I pf. First-order independent standard uncertainties; covariance is zero. Coverage factor is user supplied; the interval has no automatic confidence-level guarantee. Balanced sinusoidal system.',
    fields=(
    Field('voltage', 'Line-to-line RMS voltage', 'V', 'voltage', 400, 0, None, True, False),
    Field('current', 'RMS line current', 'A', 'current', 10, 0, None, False, False),
    Field('pf', 'Displacement power factor (lagging)', 'pu', 'ratio', 0.8, 0, 1, False, False),
    Field('u_voltage', 'Voltage standard uncertainty', 'V', 'voltage', 1, 0, None, False, False),
    Field('u_current', 'Current standard uncertainty', 'A', 'current', 0.1, 0, None, False, False),
    Field('u_pf', 'Power factor standard uncertainty', 'pu', 'ratio', 0.01, 0, None, False, False),
    Field('coverage', 'Coverage factor', 'pu', 'ratio', 2, 0, None, True, False),
    ),
    outputs={'power': 'W', 'standard_uncertainty': 'W', 'expanded_uncertainty': 'W', 'lower': 'W', 'upper': 'W'},
    formulas=('P = sqrt(3) V I pf', 'u_P² = (sqrt(3) I pf u_V)² + (sqrt(3) V pf u_I)² + (sqrt(3) V I u_pf)²', 'U = k u_P; interval = P +/- U'),
    assumptions=('First-order independent standard uncertainties; covariance is zero. Coverage factor is user supplied; the interval has no automatic confidence-level guarantee. Balanced sinusoidal system.',),
    compute=compute,
)
