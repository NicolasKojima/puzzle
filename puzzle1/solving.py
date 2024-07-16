import matplotlib.pyplot as plt
import numpy as np

# Define the pieces with correct coordinates, each covering 5 units
pieces = [
    {"label": "L1", "coordinates": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]},
    {"label": "T1", "coordinates": [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)]},
    {"label": "Z1", "coordinates": [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]},
    {"label": "C1", "coordinates": [(0, 0), (1, 0), (1, 1), (0, 1), (0, 2)]},
    {"label": "S1", "coordinates": [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]},
    {"label": "P1", "coordinates": [(0, 0), (1, 0), (0, 1), (1, 1), (2, 1)]},
    {"label": "L2", "coordinates": [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]},
    {"label": "J1", "coordinates": [(0, 0), (1, 0), (2, 0), (0, 1), (0, 2)]},
    {"label": "L3", "coordinates": [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]},
    {"label": "T2", "coordinates": [(0, 0), (1, 0), (2, 0), (1, 1), (1, 2)]},
    {"label": "Z2", "coordinates": [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]},
    {"label": "S2", "coordinates": [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]}
]

# Initialize the 8x8 board with a 2x2 block in the middle
board_size = 8
board = np.zeros((board_size, board_size), dtype=int)
middle_block = [(3, 3), (3, 4), (4, 3), (4, 4)]
for x, y in middle_block:
    board[y, x] = -1  # Mark the 2x2 block in the middle

def is_valid(board, piece, pos):
    """Check if a piece can be placed on the board at the given position."""
    px, py = pos
    for dx, dy in piece["coordinates"]:
        x, y = px + dx, py + dy
        if x < 0 or x >= board_size or y < 0 or y >= board_size or board[y, x] != 0:
            return False
    return True

def place_piece(board, piece, pos, label):
    """Place or remove a piece on the board."""
    px, py = pos
    for dx, dy in piece["coordinates"]:
        x, y = px + dx, py + dy
        board[y, x] = label

def solve(board, pieces, index=0):
    """Backtracking algorithm to solve the puzzle."""
    if index == len(pieces):
        return True
    
    piece = pieces[index]
    for y in range(board_size):
        for x in range(board_size):
            if is_valid(board, piece, (x, y)):
                place_piece(board, piece, (x, y), index + 1)
                if solve(board, pieces, index + 1):
                    return True
                place_piece(board, piece, (x, y), 0)
    
    return False

def display_board(board):
    """Display the board with the placed pieces."""
    fig, ax = plt.subplots()
    ax.set_xlim(0, board_size)
    ax.set_ylim(0, board_size)
    ax.set_xticks(np.arange(0, board_size+1, 1))
    ax.set_yticks(np.arange(0, board_size+1, 1))
    ax.grid(True)
    
    for y in range(board_size):
        for x in range(board_size):
            if board[y, x] == -1:
                rect = plt.Rectangle((x, board_size - y - 1), 1, 1, facecolor='gray')
                ax.add_patch(rect)
            elif board[y, x] > 0:
                rect = plt.Rectangle((x, board_size - y - 1), 1, 1, facecolor='lightblue', edgecolor='black')
                ax.add_patch(rect)
                ax.text(x + 0.5, board_size - y - 1 + 0.5, str(board[y, x]), color='black', ha='center', va='center')
    
    plt.show()

# Solve the puzzle
if solve(board, pieces):
    display_board(board)
else:
    print("No solution found!")
