import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell named 'TRIANGLE'
cell = lib.new_cell('TRIANGLE')

# Define the side length of the equilateral triangle (in millimeters)
side_length = 10.0  # 10 mm

# Calculate the height of the equilateral triangle
height = (math.sqrt(3) / 2) * side_length

# Calculate the vertices of the triangle centered at (0, 0)
v1 = (0, (2/3) * height)                 # Top vertex
v2 = (-side_length / 2, -height / 3)     # Bottom left vertex
v3 = (side_length / 2, -height / 3)      # Bottom right vertex

# Create the triangle polygon
triangle = gdspy.Polygon([v1, v2, v3])

# Add the triangle to the cell
cell.add(triangle)

# Save the GDSII file with units in millimeters
lib.write_gds('triangle.gds', unit=1.0e-3, precision=1.0e-9)