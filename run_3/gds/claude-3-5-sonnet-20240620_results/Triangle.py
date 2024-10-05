import gdspy
import numpy as np

# Create a new library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('TRIANGLE')

# Triangle side length in micrometers (10 mm = 10000 μm)
side_length = 10000

# Calculate triangle height
height = side_length * np.sqrt(3) / 2

# Define triangle vertices
vertices = [
    (0, 0),
    (side_length, 0),
    (side_length / 2, height)
]

# Calculate centroid
centroid = (side_length / 2, height / 3)

# Adjust vertices to center the triangle at (0, 0)
centered_vertices = [(x - centroid[0], y - centroid[1]) for x, y in vertices]

# Create the triangle polygon
triangle = gdspy.Polygon(centered_vertices)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been generated.")