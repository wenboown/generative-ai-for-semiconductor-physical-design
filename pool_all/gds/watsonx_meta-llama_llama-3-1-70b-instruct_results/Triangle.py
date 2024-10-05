import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the edge length of the equilateral triangle
edge_length = 10e3  # in micrometers

# Calculate the height of the equilateral triangle
height = edge_length * math.sqrt(3) / 2

# Calculate the coordinates of the triangle vertices
v1 = (-edge_length / 2, - height / 3)
v2 = (edge_length / 2, - height / 3)
v3 = (0, 2 * height / 3)

# Create the triangle polygon
triangle = gdspy.Polygon([v1, v2, v3])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('equilateral_triangle.gds')