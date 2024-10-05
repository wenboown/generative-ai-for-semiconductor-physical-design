import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('EQUILATERAL_TRIANGLE')

# Define the side length in micrometers (10 mm = 10,000 µm)
side_length = 10000  # in micrometers

# Calculate the height of the equilateral triangle
height = side_length * math.sqrt(3) / 2

# Compute the coordinates of the triangle's vertices
vertex1 = (0, (2/3) * height)                  # Top vertex
vertex2 = (-side_length / 2, -height / 3)      # Bottom left vertex
vertex3 = (side_length / 2, -height / 3)       # Bottom right vertex

# Create the triangle polygon
triangle = gdspy.Polygon([vertex1, vertex2, vertex3])

# Add the triangle to the cell
cell.add(triangle)

# Save the library to a GDSII file
lib.write_gds('equilateral_triangle.gds')

# Optional: View the layout using the built-in viewer (requires matplotlib)