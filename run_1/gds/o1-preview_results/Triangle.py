import gdspy
import math

# Design parameters
side_length_mm = 10  # Side length in mm
side_length_um = side_length_mm * 1000  # Convert to µm (gdspy uses µm)

# Calculate the height of the equilateral triangle
height_um = (math.sqrt(3) / 2) * side_length_um

# Calculate the vertices to center the triangle at (0, 0)
# Vertex 1 (Top vertex)
v1 = (0, (2 * height_um) / 3)
# Vertex 2 (Bottom left)
v2 = (-side_length_um / 2, -height_um / 3)
# Vertex 3 (Bottom right)
v3 = (side_length_um / 2, -height_um / 3)

# Create a new GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('EQUILATERAL_TRIANGLE')

# Create the triangle polygon
triangle = gdspy.Polygon([v1, v2, v3])

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('equilateral_triangle.gds')

print("GDS file 'equilateral_triangle.gds' has been created.")