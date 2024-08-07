import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.ndimage import measurements

# Define the shapes
shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],  # Straight Line
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # L-Shape
    [(0, 0), (0, 1), (1, 0), (2, 0), (2, 1)],  # U shape
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],  # Z shape
    [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],  # T-Shape
    [(1, 0), (1, 1), (0, 1), (2, 1), (1, 2)],  # + shape
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],  # zig zag shape
    [(0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],  # P shape
    [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)],  # short : shape
    [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1)],  # one poking out shape
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)],  # zig shape
    [(1, 0), (1, 1), (0, 1), (1, 2), (2, 2)]   # Corner Shape
]

# Function to rotate shapes 90 degrees
def rotate(shape):
    return [(y, -x) for (x, y) in shape]

# Function to mirror shapes horizontally
def mirror(shape):
    return [(-x, y) for (x, y) in shape]

# Generate all rotations and mirrors for shapes
def generate_all_rotations_and_mirrors(shape):
    rotations = [shape]
    for _ in range(3):
        rotations.append(rotate(rotations[-1]))
    mirrors = [mirror(rot) for rot in rotations]
    return rotations + mirrors

# Expand shapes to include all rotations and mirrors
all_shapes = [generate_all_rotations_and_mirrors(shape) for shape in shapes]

def can_place(board, shape, x, y):
    for (dx, dy) in shape:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 8 and 0 <= ny < 8) or board[ny, nx] != 0:
            return False
    return True

def place_shape(board, shape, x, y, value):
    for (dx, dy) in shape:
        board[y + dy, x + dx] = value

def remove_shape(board, shape, x, y):
    for (dx, dy) in shape:
        board[y + dy, x + dx] = 0

def plot_board(board, ax):
    ax.clear()
    ax.imshow(board, cmap='tab20', origin='upper')
    ax.grid(which='both', color='grey', linestyle='-', linewidth=1)
    ax.set_xticks(np.arange(-.5, 8, 1))
    ax.set_yticks(np.arange(-.5, 8, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.pause(0.5)

def has_small_empty_spaces(board):
    empty_space_mask = (board == 0).astype(int)
    labeled_array, num_features = measurements.label(empty_space_mask)
    for i in range(1, num_features + 1):
        if np.sum(labeled_array == i) < 5:
            return True
    return False

def solve(board, all_shapes, index=0, ax=None):
    if index == len(all_shapes):
        return True

    for y in range(8):
        for x in range(8):
            for shape in all_shapes[index]:
                if can_place(board, shape, x, y):
                    place_shape(board, shape, x, y, index + 1)
                    plot_board(board, ax)
                    if not has_small_empty_spaces(board):
                        if solve(board, all_shapes, index + 1, ax):
                            return True
                    remove_shape(board, shape, x, y)
                    plot_board(board, ax)
    
    return False

# Initialize the board and mark the 2x2 center as occupied
board = np.zeros((8, 8), dtype=int)
board[3:5, 3:5] = -1  # Mark the 2x2 center block

# Plot the initial board
fig, ax = plt.subplots(figsize=(6, 6))
plot_board(board, ax)

# Try to solve the puzzle
if solve(board, all_shapes, ax=ax):
    print("Solution found:")
else:
    print("No solution found.")

plt.show()
