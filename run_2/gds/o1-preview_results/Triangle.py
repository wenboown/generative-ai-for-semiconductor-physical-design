import gdspy
import math

# Units are in micrometers (since GDSII uses micrometers)
# Define the side length of the triangle
side_length = 10000  # 10 mm = 10,000 micrometers

# Calculate the height of the equilateral triangle
height = (math.sqrt(3) / 2) * side_length

# Calculate the coordinates of the triangle's vertices to center it at (0, 0)
vertex1 = (0, (2/3) * height)  # Top vertex
vertex2 = (-side_length / 2, -height / 3)  # Bottom left vertex
vertex3 = (side_length / 2, -height / 3)  # Bottom right vertex

# Define the points of the triangle
triangle_points = [vertex1, vertex2, vertex3]

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a cell to contain the triangle
cell = lib.new_cell('EQUILATERAL_TRIANGLE')

# Create the triangle polygon
triangle = gdspy.Polygon(triangle_points, layer=0)

# Add the triangle to the cell
cell.add(triangle)

# Save the library in a GDSII file
lib.write_gds('equilateral_triangle.gds')