import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Function to create a square
def create_square(x, y, size):
    return gdspy.Rectangle((x, y), (x + size, y + size))

# Parameters
square_size = 5  # 5 mm
spacing = 20  # 20 mm
rows = 10
cols = 10

# Calculate the starting position (bottom-left corner of the entire array)
start_x = -spacing * (cols - 1)
start_y = -spacing * (rows - 1)

# Create and add squares to the cell
for row in range(rows):
    for col in range(cols):
        x = start_x + col * spacing
        y = start_y + row * spacing
        square = create_square(x, y, square_size)
        cell.add(square)

# Save the design to a GDS file
lib.write_gds('square_array.gds')

# Optional: View the layout