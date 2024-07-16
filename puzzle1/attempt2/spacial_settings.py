import matplotlib.pyplot as plt
import numpy as np

# Define the shapes as lists of coordinates
shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],  # Straight Line
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # L-Shape
    [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],  # U shape
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],  # Z shape
    [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],  # T-Shape
    [(1, 0), (1, 1), (0, 1), (2, 1), (1, 2), (2, 1)],  # + shape
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],  # zig zag shape
    [(0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],  # P shape
    [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],  # short : shape
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)],  # one poking out shape
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)],  # zig shape
    [(1, 0), (1, 1), (0, 1), (1, 2), (2, 2)]   # Corner Shape
]

def plot_shape(shape, ax):
    grid = np.zeros((5, 5))
    for (x, y) in shape:
        grid[y, x] = 1
    ax.imshow(grid, cmap='Greens', origin='upper')
    ax.grid(which='both', color='gray', linestyle='-', linewidth=1)
    ax.set_xticks(np.arange(-.5, 5, 1))
    ax.set_yticks(np.arange(-.5, 5, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

fig, axes = plt.subplots(3, 4, figsize=(12, 9))
axes = axes.flatten()

for i, shape in enumerate(shapes):
    plot_shape(shape, axes[i])

plt.tight_layout()
plt.show()
