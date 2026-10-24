"""RMS phasors: ABC positive sequence and exp(j omega t) convention."""
import cmath
from math import radians, sqrt

def polar(magnitude, angle_deg):
    return cmath.rect(magnitude, radians(angle_deg))

def phases(line_voltage):
    v = line_voltage / sqrt(3)
    return polar(v, 0), polar(v, -120), polar(v, 120)

def sequences(a_phase, b_phase, c_phase):
    a = polar(1, 120)
    return ((a_phase+b_phase+c_phase)/3,
            (a_phase+a*b_phase+a*a*c_phase)/3,
            (a_phase+a*a*b_phase+a*c_phase)/3)

def reconstruct(zero, positive, negative):
    a = polar(1, 120)
    return zero+positive+negative, zero+a*a*positive+a*negative, zero+a*positive+a*a*negative

def nonzero(z, name='Impedance'):
    if abs(z) == 0:
        raise ValueError(name + ' must not be zero')
    return z
