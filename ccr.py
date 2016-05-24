import math

"""CNS% Load (per/min) at given ppO2"""
CNS_TABLE = { 0.60: 0.14,
              0.70: 0.18,
              0.75: 0.20,
              0.80: 0.22,
              0.85: 0.25,
              0.90: 0.28,
              0.95: 0.30,
              1.00: 0.33,
              1.05: 0.37,
              1.10: 0.42,
              1.15: 0.44,
              1.20: 0.47,
              1.25: 0.51,
              1.30: 0.56,
              1.35: 0.61,
              1.40: 0.65,
              1.45: 0.72,
              1.50: 0.83,
              1.55: 1.11,
              1.60: 2.22 }

"""OTU Units (per/min) at given ppO2"""
OTU_TABLE = { 0.60: 0.26,
              0.70: 0.47,
              0.75: 0.56,
              0.80: 0.65,
              0.85: 0.74,
              0.90: 0.83,
              0.95: 0.92,
              1.00: 1.00,
              1.05: 1.08,
              1.10: 1.16,
              1.15: 1.24,
              1.20: 1.32,
              1.25: 1.40,
              1.30: 1.48,
              1.35: 1.55,
              1.40: 1.63,
              1.45: 1.70,
              1.50: 1.78,
              1.55: 1.85,
              1.60: 1.92 }

def percinbag(setpoint, depth):
    """Returns the approximate percentage of Oxygen in the loop for a given setpoint and depth."""
    absp = int(depth)/10 + 1
    return round(setpoint / absp * 100, 2)

def mod(perco2, desired_max_po2):
    """Returns the Max Operating Depth of a breathing gas, for a desired maximum partial pressure of Oxygen."""
    abs_mod = desired_max_po2 / (perco2/100)
    return math.floor((abs_mod-1) * 10)

def ead(setpoint, depth):
    Fn2 = (100 - percinbag(setpoint, depth))/100
    return math.floor(((depth+10) * (Fn2/0.79)) - 10)

def decantNx(supply_capacity, supply_pressure, supply_mix, receive_capacity, receive_pressure, receive_mix):
    """Returns the new pressure and Oxygen content of a decanting operation as tuple (pressure, O2%)."""
    pass
        
