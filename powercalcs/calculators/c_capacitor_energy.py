"""Stored capacitor energy. See docs/calculators/capacitor_energy.md."""
from math import sqrt, hypot, pi, acos, tan, atan2, degrees
from cmath import rect
from powercalcs.engine import Calculator, Field
from powercalcs.phasors import phases, sequences, reconstruct, nonzero

def compute(capacitance, instant_voltage):
    return dict(energy=.5*capacitance*instant_voltage**2,charge=capacitance*instant_voltage)

CALCULATOR = Calculator(
    id='capacitor_energy', title='Stored capacitor energy', category='Capacitors',
    description='E = (1/2) C v². Voltage is instantaneous or DC, not RMS. Single ideal capacitor; dielectric losses omitted.',
    fields=(
    Field('capacitance', 'Capacitance', 'F', 'capacitance', 0.001, 0, None, False, False),
    Field('instant_voltage', 'Instantaneous/DC voltage', 'V', 'voltage', 400, 0, None, False, False),
    ),
    outputs={'energy': 'J', 'charge': 'C'},
    formulas=('E = (1/2) C v²', 'q = C v'),
    assumptions=('Voltage is instantaneous or DC, not RMS. Single ideal capacitor; dielectric losses omitted.',),
    compute=compute,
)
