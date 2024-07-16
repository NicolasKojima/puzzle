import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Manually define the coordinates and shapes of each piece
pieces = [
    {"label": "L1", "coordinates": [(0, 0), (1, 0), (2, 0), (2, 1)]},
    {"label": "T1", "coordinates": [(0, 0), (1, 0), (2, 0), (1, 1)]},
    {"label": "Z1", "coordinates": [(0, 0), (1, 0), (1, 1), (2, 1)]},
    {"label": "C1", "coordinates": [(0, 0), (1, 0), (1, 1), (0, 1)]},
    {"label": "S1", "coordinates": [(0, 1), (1, 1), (1, 0), (2, 0)]},
    {"label": "P1", "coordinates": [(1, 0), (0, 1), (1, 1), (1, 2), (2, 1)]},
    {"label": "L2", "coordinates": [(0, 0), (0, 1), (0, 2), (1, 2)]},
    {"label": "J1", "coordinates": [(0, 0), (1, 0), (2, 0), (0, 1)]},
    {"label": "L3", "coordinates": [(0, 0), (1, 0), (2, 0), (2, 1)]},
    {"label": "T2", "coordinates": [(0, 1), (1, 0), (1, 1), (1, 2)]},
    {"label": "Z2", "coordinates": [(0, 1), (1, 1), (1, 0), (2, 0)]},
    {"label": "S2", "coordinates": [(0, 0), (1, 0), (1, 1), (2, 1)]}
]

# Loop through each piece and create a plot for each one
for piece in pieces:
    fig, ax = plt.subplots()
    label = piece["label"]
    coordinates = piece["coordinates"]
    for coord in coordinates:
        rect = Rectangle((coord[0], -coord[1]), 1, 1, linewidth=1, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    # Label the piece
    ax.text(coordinates[0][0] + 0.5, -coordinates[0][1] - 0.5, label, color='b', weight='bold', ha='center', va='center')
    
    # Set the limits and grid
    ax.set_xlim(-1, 4)
    ax.set_ylim(-5, 1)
    ax.set_aspect('equal')
    ax.grid(True)
    
    # Show the plot
    plt.gca().invert_yaxis()
    plt.title(f"Piece {label}")
    plt.show()
    # Save the plot (optional)
    # plt.savefig(f"{label}.png")
