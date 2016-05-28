"""Gas blending functions (Very approximate).
Whenever a function calls for a gas mix it must be tuple in form (O2%, He%) e.g.
    18/35Tx would be (18, 35)
    Air would be (21, 00)
    32% Nitrox would be (32, 00)."""
import math
from . import utils

def decant(s_cyl_size, s_cyl_pressure, r_cyl_size, r_cyl_pressure):
    """Returns cylinder pressures after decant."""
    total_vol = s_cyl_size + r_cyl_size
    s_lts = s_cyl_size * s_cyl_pressure
    r_lts = r_cyl_size * r_cyl_pressure
    return (s_lts + r_lts) / total_vol

def decantTx(s_cyl_size, s_cyl_pressure, s_mix, r_cyl_size, r_cyl_pressure, r_mix):
    """Non-air decanting, mix inputs are tuples (O2,He) and returns tuple in form ((O2,He), pressure).
Restuls rounded to nearest 0.05 for gas percentages."""
    # Lts of each component gas in receiving cylinder.
    r_gas = r_cyl_size * r_cyl_pressure
    r_o2 = r_gas/100 * r_mix[0]
    r_He = r_gas/100 * r_mix[1]
    
    # Get final presure to work out volume of gas added.
    final = decant(s_cyl_size, s_cyl_pressure, r_cyl_size, r_cyl_pressure)

    # volume of gas supplied to other cylinder (lts).
    vol = (s_cyl_pressure - final) * s_cyl_size

    # Volume of supplied gasses.
    supplied_o2 = vol/100 * s_mix[0]
    supplied_He = vol/100 * s_mix[1]

    # Final gas volumes and %.
    final_o2 = r_o2 + supplied_o2
    final_He = r_He + supplied_He
    
    final_r_vol = final * r_cyl_size    
    final_o2_perc = final_o2/final_r_vol * 100
    final_he_perc = final_He/final_r_vol * 100

    return ((utils.round_to(final_o2_perc, 0.05), utils.round_to(final_he_perc, 0.05)), utils.round_to(final, 0.5))
    

def topup(cyl_size, cyl_pressure, current_mix, filling_mix, final_pressure):
    """Topping up from a compressor."""
    pass


