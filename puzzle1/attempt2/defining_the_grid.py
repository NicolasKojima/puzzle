import matplotlib.pyplot as plt
import numpy as np

def plot_grid(ax):
    grid = np.ones((8, 8))  # Initialize the grid with ones (white)
    grid[3:5, 3:5] = 0  # Create a 2x2 black space in the middle
    ax.imshow(grid, cmap='gray', origin='upper')
    
    # Create grey grid lines for the entire 8x8 grid
    ax.grid(which='both', color='grey', linestyle='-', linewidth=2)
    ax.set_xticks(np.arange(-.5, 8, 1))
    ax.set_yticks(np.arange(-.5, 8, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

fig, ax = plt.subplots(figsize=(6, 6))

# Plot the grid with the specified colors
plot_grid(ax)

plt.tight_layout()
plt.show()
