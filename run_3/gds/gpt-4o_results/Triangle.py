import gdspy
import numpy as np

# Create a new GDSII library named 'library'
lib = gdspy.GdsLibrary()

# Create a new cell in the library
cell = lib.new_cell('TRIANGLE')

# Define the coordinates for an equilateral triangle centered at (0, 0)
side_length = 10
height = (np.sqrt(3) / 2) * side_length

center_x, center_y = 0, 0  # Center of the triangle

# Calculate vertex positions
vertices = [
    (center_x - side_length / 2, center_y - height / 3),
    (center_x + side_length / 2, center_y - height / 3),
    (center_x, center_y + 2 * height / 3)
]

# Create the polygon
triangle = gdspy.Polygon(vertices, layer=1)

# Add the triangle to the cell
cell.add(triangle)

# Save the library to a GDS file
lib.write_gds('triangle.gds')

print("GDS file 'triangle.gds' has been created with a triangle centered at (0,0) with edges of 10 mm.")