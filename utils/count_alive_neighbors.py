"""
This function will compute the number of living neighbors for the cell at given x,y in the given world state. You can also pass in an option for whether or not you want to include world wrapping.
Created - Jun/19/2026 
"""

import numpy as np

def count_alive_neighbors(world_state,x,y):

    # ----- Initialize Local Variables -----
    num_alive_neighbors = 0

    # ----- Loop Through All Neighbor Cells -----
    for xi in range(3):
        for yi in range(3):

            # ----- Dont Count The Cell of Interest -----
            if xi==1 and yi==1:
                continue

            # ----- Non-Wrapping Mode -----
            xidx = x-1+xi
            yidx = y-1+yi
            if xidx>-1 and yidx>-1 and xidx<world_state.shape[0] and yidx<world_state.shape[1]:
                if world_state[xidx,yidx]==1:
                    num_alive_neighbors += 1

    # ----- Return Number of Alive Neighbors -----
    return num_alive_neighbors
                
        
    