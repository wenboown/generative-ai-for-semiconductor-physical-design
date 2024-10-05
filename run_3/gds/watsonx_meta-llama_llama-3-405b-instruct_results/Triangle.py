import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the coordinates for the triangle
edge_length = 10  # mm
center_x, center_y = 0, 0
half_edge = edge_length / 2
height = math.sqrt(edge_length**2 - half_edge**2)

# Create the triangle
points = [
    (center_x - half_edge, center_y - height/3),
    (center_x, center_y + 2*height/3),
    (center_x + half_edge, center_y - height/3)
]
triangle = gdspy.Polygon(points, layer=1)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')