import gdspy
import numpy as np

# Create a new library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRIANGLE')

# Calculate the coordinates of the triangle vertices
side_length = 10000  # 10 mm in micrometers
height = side_length * np.sqrt(3) / 2
half_side = side_length / 2

# Calculate vertex coordinates
v1 = (-half_side, -height/3)
v2 = (half_side, -height/3)
v3 = (0, 2*height/3)

# Create a polygon for the triangle
triangle = gdspy.Polygon([v1, v2, v3])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been generated.")