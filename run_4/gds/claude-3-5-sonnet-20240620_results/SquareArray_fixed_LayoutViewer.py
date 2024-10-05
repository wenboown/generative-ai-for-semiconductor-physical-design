import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_ARRAY')

# Define square size and spacing
square_size = 5000  # 5 mm in nanometers
spacing = 20000  # 20 mm in nanometers

# Calculate the starting position for the upper right square
start_x = 0 - square_size
start_y = 0 - square_size

# Create the array of squares
for i in range(10):
    for j in range(10):
        x = start_x - j * spacing
        y = start_y - i * spacing
        square = gdspy.Rectangle((x, y), (x + square_size, y + square_size))
        cell.add(square)

# Save the layout to a GDS file
lib.write_gds('square_array.gds')

# Optional: View the layout