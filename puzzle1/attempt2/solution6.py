import numpy as np
import matplotlib.pyplot as plt
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

# Function to check if shape can be placed at (x, y) on board
def can_place(board, shape, x, y):
    for (dx, dy) in shape:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < 8 and 0 <= ny < 8) or board[ny, nx] != 0:
            return False
    return True

# Function to place shape on board
def place_shape(board, shape, x, y, value):
    for (dx, dy) in shape:
        board[y + dy, x + dx] = value

# Function to remove shape from board
def remove_shape(board, shape, x, y):
    for (dx, dy) in shape:
        board[y + dy, x + dx] = 0

# Function to check if board has valid empty spaces
def has_valid_empty_spaces(board):
    empty_space_mask = (board == 0).astype(int)
    labeled_array, num_features = measurements.label(empty_space_mask)
    for i in range(1, num_features + 1):
        if np.sum(labeled_array == i) % 5 != 0:
            return False
    return True

# Function to solve the puzzle
def solve(board, all_shapes, index=0):
    if index == len(all_shapes):
        return True

    for y in range(8):
        for x in range(8):
            for shape in all_shapes[index]:
                if can_place(board, shape, x, y):
                    place_shape(board, shape, x, y, index + 1)
                    if has_valid_empty_spaces(board):  # Check board validity
                        if solve(board, all_shapes, index + 1):
                            return True
                    remove_shape(board, shape, x, y)
    
    return False

# Initialize the board and mark the 2x2 center as occupied
board = np.zeros((8, 8), dtype=int)
board[3:5, 3:5] = -1  # Mark the 2x2 center block

# Try to solve the puzzle
if solve(board, all_shapes):
    print("Solution found:")
else:
    print("No solution found.")
