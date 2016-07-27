"""Data used by other modules and conversion functions."""
import math

"""CNS% Load dictionary (ppO2:CNS% per min)."""
CNS_TABLE = { 0.60: 0.14,
              0.65: 0.16,
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

"""OTU Units dictionary (ppO2:OTU per min)."""
OTU_TABLE = { 0.60: 0.26,
              0.65: 0.39,
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

def round_to(n, base=0.05):
    """rounds a number to a given prescision. E.g. (32.7, 0.5) = 32.5"""
    return round(base*round(n/base), 2)

def mod(percent_O2, desired_max_pO2):
    """Returns the Max Operating Depth of a breathing gas, for a desired maximum partial pressure of Oxygen."""
    abs_mod = desired_max_pO2 / (percent_O2/100)
    return math.floor((abs_mod-1) * 10)

def cns(ppO2, time):
    """Returns ceiling CNS% for a given ppO2 & time"""
    if ppO2 > 1.6 or ppO2 < 0.6:
        raise Exception('ppO2 outside range (0.6-1.6)')
    return round_to(CNS_TABLE[round_to(ppO2)]*time, 0.5)

def otu(ppO2, time):
    """Return OTU for a given ppO2 & time"""
    if ppO2 > 1.6 or ppO2 < 0.6:
        raise Exception('ppO2 outside range (0.6-1.6)')
    return round_to(OTU_TABLE[round_to(ppO2)]*time, 0.5)

def toPSI(bar):
    """Imperial suppport function, turn BAR into PSI."""
    return bar*14.504

def toBAR(psi):
    """Imperial suppport function, turn PSI into BAR."""
    return psi/14.504

def toFeet(metres):
    """Imperial suppport function, turn Metres into Feet."""
    return metres*3.281

def toMts(feet):
    """Imperial suppport function, turn Feet into Metres."""
    return feet*0.3048

def toFarenheit(celsius):
    """Imperial suppport function, turn degrees C into degrees F."""
    return (celsius*1.8)+32

def toCelsius(farenheit):
    """Imperial suppport function, turn degrees F into degrees C."""
    return (farenheit-32)/1.8


