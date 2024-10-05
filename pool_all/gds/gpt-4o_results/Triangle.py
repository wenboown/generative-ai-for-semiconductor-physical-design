import gdspy
import numpy as np

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell for the triangle
cell = lib.new_cell('EQUILATERAL_TRIANGLE')

# Triangle side length in micrometers
side_length = 10000  # 10 mm = 10,000 micrometers

# Calculate the height of the triangle
height = side_length * np.sqrt(3) / 2

# Define vertices for an equilateral triangle centered at the origin
vertices = [
    (-side_length / 2, -height / 3),
    (side_length / 2, -height / 3),
    (0, 2 * height / 3)
]

# Create the polygon
triangle = gdspy.Polygon(vertices, layer=1)

# Add the triangle to the cell
cell.add(triangle)

# Write the GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been generated successfully.")