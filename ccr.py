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

def best_bailout(depth):
    """returns the best bottom bailout O2% for depth (max 1.6 BAR ppO2)."""
    return math.floor(percinbag(1.6,depth))

def dive(max_depth, dive_time, low_sp, high_sp):
    """Prints a report for a dive."""
    print("CNS:\t\t" + str(utils.cns(high_sp+0.05, dive_time)) + "%")
    print("OTU:\t\t" + str(utils.otu(high_sp+0.05, dive_time)))
    print("Best Bailout:\t" + str(best_bailout(max_depth)) + "% O2")



        
