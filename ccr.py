"""Contains functions for rebreather dive planning."""

import math
from . import utils

def percinbag(setpoint, depth):
    """Returns the approximate percentage of Oxygen in the loop for a given setpoint and depth."""
    absp = int(depth)/10 + 1
    return round(setpoint / absp * 100, 2)

def ead(setpoint, depth):
    """Gives equivalent air depth for a given setpoint using air diluent."""
    Fn2 = (100 - percinbag(setpoint, depth))/100
    return math.floor(((depth+10) * (Fn2/0.79)) - 10)

def dive(max_depth, dive_time, low_sp, high_sp):
    """Prints a report for a dive."""
    print("CNS%:\t\t" + str(utils.cns(high_sp, dive_time)))
    print("OTU :\t\t" + str(utils.otu(high_sp, dive_time)))
    print("Best Bailout:\tTODO")



        
