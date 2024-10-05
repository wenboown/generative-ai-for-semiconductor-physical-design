import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('EQUILATERAL_TRIANGLE')

# Side length in micrometers (10 mm = 10,000 µm)
s = 10000.0  # Side length

# Calculate the height of the equilateral triangle
h = (math.sqrt(3) / 2) * s

# Calculate the vertices of the triangle centered at (0, 0)
vertex1 = (0, (2/3) * h)
vertex2 = (-s / 2, - (1/3) * h)
vertex3 = (s / 2, - (1/3) * h)

# Create the triangle as a polygon
triangle = gdspy.Polygon([vertex1, vertex2, vertex3])

# Add the polygon to the cell
cell.add(triangle)

# Save the library to a GDSII file
lib.write_gds('equilateral_triangle.gds')

# Optional: View the layout using gdspy's built-in viewer (uncomment to use)
bash
pip install gdspy