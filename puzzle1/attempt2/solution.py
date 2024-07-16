import numpy as np
import matplotlib.pyplot as plt

# Define the shapes and their possible rotations
shapes = [
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],  # Straight Line
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)],  # L-Shape
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],  # Mirrored L-Shape
    [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)],  # Another Mirrored L-Shape
    [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)],  # T-Shape
    [(0, 0), (1, 0), (2, 0), (1, 1), (0, 1)],  # Plus Shape
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],  # Z-Shape
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)],  # Mirrored Z-Shape
    [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1)],  # S-Shape
    [(0, 0), (0, 1), (0, 2), (1, 0), (2, 0)],  # U-Shape
    [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)],  # C-Shape
    [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]   # Corner Shape
]

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

def solve(board, shapes, index=0):
    if index == len(shapes):
        return True

    for y in range(8):
        for x in range(8):
            if can_place(board, shapes[index], x, y):
                place_shape(board, shapes[index], x, y, index + 1)
                if solve(board, shapes, index + 1):
                    return True
                remove_shape(board, shapes[index], x, y)
    
    return False

# Initialize the board and mark the 2x2 center as occupied
board = np.zeros((8, 8), dtype=int)
board[3:5, 3:5] = -1  # Mark the 2x2 center block

# Try to solve the puzzle
if solve(board, shapes):
    print("Solution found:")
else:
    print("No solution found.")

# Plot the solution
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(board, cmap='tab20', origin='upper')
ax.grid(which='both', color='grey', linestyle='-', linewidth=1)
ax.set_xticks(np.arange(-.5, 8, 1))
ax.set_yticks(np.arange(-.5, 8, 1))
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.tight_layout()
plt.show()
