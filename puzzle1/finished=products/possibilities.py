import numpy as np

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
    all_variants = rotations + mirrors
    # Remove duplicate shapes
    all_variants = [tuple(sorted(variant)) for variant in all_variants]
    return list(set(all_variants))

# Expand shapes to include all rotations and mirrors
all_shapes = [generate_all_rotations_and_mirrors(shape) for shape in shapes]

# Calculate the total number of possible combinations
total_combinations = 1
for shape_variants in all_shapes:
    total_combinations *= len(shape_variants)

print(f"Total possible combinations: {total_combinations}")