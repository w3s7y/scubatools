"""Gas blending functions (using ideal gas laws)."""
import math

def decant(s_cyl_size, s_cyl_pressure, r_cyl_size, r_cyl_pressure):
    """Returns cylinder pressures after decant.  Assumes same gas mix in supply and recieve cylinders."""
    total_vol = s_cyl_size + r_cyl_size
    s_lts = s_cyl_size * s_cyl_pressure
    r_lts = r_cyl_size * r_cyl_pressure
    return math.floor((s_lts + r_lts) / total_vol)

def decantNx(s_cyl_size, s_cyl_pressure, s_cyl_O2, r_cyl_size, r_cyl_pressure, r_cyl_O2):
    """Nitrox decanting, returns tuple in form (pressure, O2% in receive)."""
    final_pressure = decant(s_cyl_size, s_cyl_pressure, r_cyl_size, r_cyl_pressure)
    return (final_pressure, 'TODO')

def decantTx(s_cyl_size, s_cyl_pressure, s_cyl_O2, s_cyl_He, r_cyl_size, r_cyl_pressure, r_cyl_O2, r_cyl_He):
    """Trimix decanting, returns dictionary in form { 'O2' : <o2perc>, 'He' : <HePerc>, 'Pressure' : <final_pressure> }."""
    return { 'O2' : 'TODO', 'He' : 'TODO', 'Pressure' : 'TODO' }

def topup(pressure, size, current_mix, filling_gas, final_pressure):
    """Topping up from a compressor. is a number (int/float) it is assumed to be O2% of a nitrox mix.
If it is a tuple, it is assumed to be (O2,He) Trimix.

