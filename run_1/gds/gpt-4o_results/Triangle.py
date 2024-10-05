import gdspy

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('TRIANGLE')

# Define the equilateral triangle
# The height of an equilateral triangle is `sqrt(3)/2 * side_length`
import math

side_length = 10000  # 10 mm in micrometers (as GDSII uses microns)
height = math.sqrt(3) / 2 * side_length

# Vertices of the equilateral triangle centered at (0, 0)
p1 = (-side_length / 2, -height / 3)
p2 = (side_length / 2, -height / 3)
p3 = (0, 2 * height / 3)

# Add the triangle to the cell
polygon = gdspy.Polygon([p1, p2, p3])
cell.add(polygon)

# Write the GDS to a file
gdspy.write_gds('triangle.gds', [cell])

print("GDS file 'triangle.gds' generated successfully.")