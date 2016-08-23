"""Contains functions for rebreather dive planning."""
import math
from . import utils


# Quick and easy functions.
def percinbag(setpoint, depth):
    """Returns the approximate percentage of Oxygen in the loop for a given setpoint and depth."""
    absp = depth/10 + 1
    return round(setpoint / absp * 100, 2)

def ead(setpoint, depth):
    """Gives equivalent air depth for a given setpoint using air diluent (or OC nitrox)."""
    Fn2 = (100 - percinbag(setpoint, depth))/100
    return round(((depth+10) * (Fn2/0.79)) - 10, 2)

def end(setpoint, depth, diluent):
    """Equivalent narcotic depth for trimix diluents."""
    FHe = diluent[1] / 100
    return round(((depth+10) * (1 - FHe)) - 10, 2)

def best_bailout(depth):
    """returns the best bottom bailout O2% for depth (max 1.6 BAR ppO2)."""
    return math.floor(percinbag(1.6,depth))

def dive(max_depth, dive_time, low_sp, high_sp):
    """Prints a report for a dive with the CNS% and OTU loads.
Also the best bailout for the depth."""
    print("CNS:\t\t" + str(utils.cns(high_sp+0.05, dive_time)) + "%")
    print("OTU:\t\t" + str(utils.otu(high_sp+0.05, dive_time)))
    print("Best Bailout:\t" + str(best_bailout(max_depth)) + "% O2")
    if max_depth >= 16:
        print("EAD:\t\t" + str(ead(high_sp, max_depth)) + "M")
    else:
        print("EAD:\t\t" + str(ead(low_sp, max_depth)) + "M")



class ccr_config:
    # Default APD unit settings.
    upDepth = 16
    downDepth = 4
    
    
    """Class that represents a eCCRs Configuration."""
    def __init__(upDepth, downDepth):
        """Initialization method."""
        
