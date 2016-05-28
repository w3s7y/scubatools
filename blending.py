"""Gas blending functions (using ideal gas laws)."""
import math

def decant(s_cyl_size, s_cyl_pressure, r_cyl_size, r_cyl_pressure):
    """Returns cylinder pressures after decant.  Assumes same gas mix in supply and recieve cylinders."""
    total_vol = s_cyl_size + r_cyl_size
    s_lts = s_cyl_size * s_cyl_pressure
    r_lts = r_cyl_size * r_cyl_pressure
    return int(math.floor((s_lts + r_lts) / total_vol))

def decantTx(s_cyl_size, s_cyl_pressure, s_mix, r_cyl_size, r_cyl_pressure, r_mix):
    """Non-air decanting, mix inputs are tuple (O2,He) and returns tuple in form ((O2,He), pressure)"""
    # The supply cylinder component gas volumes.
    s_gas = s_cyl_size * s_cyl_pressure
    s_o2 = s_gas/100 * s_mix[0]
    s_He = s_gas/100 * s_mix[1]

    # Same for receiving cylinder
    r_gas = r_cyl_size * r_cyl_pressure
    r_o2 = r_gas/100 * r_mix[0]
    r_He = r_gas/100 * r_mix[1]
    

    
    

def topup(pressure, size, current_mix, filling_gas, final_pressure):
    """Topping up from a compressor. is a number (int/float) it is assumed to be O2% of a nitrox mix.
If it is a tuple, it is assumed to be (O2,He) Trimix."""
    pass

