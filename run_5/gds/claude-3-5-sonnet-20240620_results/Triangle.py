import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRIANGLE')

# Calculate triangle dimensions
side_length = 10000  # 10 mm in nanometers
height = side_length * np.sqrt(3) / 2
half_width = side_length / 2

# Define triangle vertices
vertices = [
    (0, height / 2),
    (-half_width, -height / 2),
    (half_width, -height / 2)
]

# Create the triangle polygon
triangle = gdspy.Polygon(vertices, layer=0)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been generated.")