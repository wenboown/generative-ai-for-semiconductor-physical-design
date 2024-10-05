import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('triangle')

# Define the triangle's edge length and center coordinates
edge_length = 10
center_x, center_y = 0, 0

# Calculate the coordinates of the triangle's vertices
vertices = []
for i in range(3):
    angle = 2 * math.pi / 3 * i
    x = center_x + edge_length / 2 * math.cos(angle)
    y = center_y + edge_length / 2 * math.sin(angle)
    vertices.append((x, y))

# Create the triangle polygon
triangle = gdspy.Polygon(vertices)

# Add the triangle to the cell
cell.add(triangle)

# Save the design to a GDS file
lib.write_gds('triangle.gds')