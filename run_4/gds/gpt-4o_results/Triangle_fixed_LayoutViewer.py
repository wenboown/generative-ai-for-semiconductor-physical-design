import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Define the cell where the triangle will be drawn
cell = lib.new_cell('TRIANGLE')

# Triangle side length
side_length = 10000  # in micrometers (1 mm = 1000 micrometers)

# Calculate the height of the equilateral triangle
height = (math.sqrt(3) / 2) * side_length

# Define the vertices of the triangle centered at (0, 0)
v1 = (-side_length / 2, -height / 3)
v2 = (side_length / 2, -height / 3)
v3 = (0, 2 * height / 3)

# Create the triangle polygon
triangle = gdspy.Polygon([v1, v2, v3])

# Add the triangle to the cell
cell.add(triangle)

# Write the GDS file
lib.write_gds('triangle.gds')

# Optionally, view the layout using gdspy internal viewer