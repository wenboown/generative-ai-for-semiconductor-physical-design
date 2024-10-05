import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('SQUARE_WITH_ROUNDED_CORNERS')

# Define the square dimensions (in micrometers)
width = 10000  # 10 mm = 10000 µm
height = 10000  # 10 mm = 10000 µm

# Define the corner radius (in micrometers)
radius = 1000  # 1 mm = 1000 µm

# Create the square as a polygon
square = gdspy.Rectangle((0, 0), (width, height))

# Apply corner rounding
rounded_square = gdspy.round_corners(square, radius)

# Add the rounded square to the cell
cell.add(rounded_square)

# Save the design to a GDS file
lib.write_gds('square_with_rounded_corners.gds')

print("GDS file 'square_with_rounded_corners.gds' has been created.")