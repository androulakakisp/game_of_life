"""
This file will run a custom implementation of John Conway's Game of Life. Many of the world paremters are hard coded so you can modify them below if you want to mess around with things.
"""

# ===================
# ----- Imports -----
# ===================
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from utils.count_alive_neighbors import count_alive_neighbors

# ================================
# ----- Set World Parameters -----
# ================================
world_size = (50,50)
world_wrap = True
time_steps = 100

# ===============================
# ----- Initial World State -----
# ===============================
world_state = np.zeros(world_size)
world_state[1, 2] = 1
world_state[2, 3] = 1
world_state[3, 1] = 1
world_state[3, 2] = 1
world_state[3, 3] = 1
print(world_state)

# ===============================
# ----- Initialize Plotting -----
# ===============================
fig, ax = plt.subplots()
ax.axis('off')
frames = []


# ============================
# ----- Run Through Time -----
# ============================
for t in range(time_steps):

    # ----- Take Snapshot for Animation -----
    img = ax.imshow(world_state, cmap='binary', interpolation='nearest')
    frames.append([img])

    # ----- Loop Thorugh Every Cell -----
    next_world_state = np.zeros(world_size)
    for x in range(world_size[0]):
        for y in range(world_size[1]):

            cell_alive = world_state[x,y]
            num_alive_neighbors = count_alive_neighbors(world_state,x,y)

            # ----- Rule 1 -----
            # Kill the cell if it has 1 or fewer alive neighbors
            if cell_alive==1 and num_alive_neighbors==1:
                next_world_state[x,y] = 0

            # ----- Rule 2 -----
            # Kill the cell if it has 4 or more alive neighbors
            elif cell_alive==1 and num_alive_neighbors>=4:
                next_world_state[x,y] = 0

            # ----- Rule 3 -----
            # Leave the cell alive if it has 2 or 3 alive neighbors
            elif cell_alive==1 and (num_alive_neighbors==2 or num_alive_neighbors==3):
                next_world_state[x,y] = 1

            # ----- Rule 4 -----
            # Bring the cell to life if it was dead and has 3 alive neighbors
            elif cell_alive==0 and num_alive_neighbors==3:
                next_world_state[x,y] = 1

    world_state = next_world_state
    print(world_state)

# ===================================
# ----- Compile and Save to GIF -----
# ===================================
ani = animation.ArtistAnimation(fig, frames, interval=200, blit=True, repeat_delay=1000)
ani.save('game_of_life.gif', writer='pillow')




            

# %%
