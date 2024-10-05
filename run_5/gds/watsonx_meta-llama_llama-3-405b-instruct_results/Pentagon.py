import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon')

# Define the edge length and center coordinates
edge_length = 10
center_x, center_y = 0, 0

# Calculate the angle and coordinates for each vertex
angle = 2 * math.pi / 5
vertices = []
for i in range(5):
    x = center_x + edge_length / 2 * math.cos(i * angle)
    y = center_y + edge_length / 2 * math.sin(i * angle)
    vertices.append((x, y))

# Create a polygon for the pentagon
poly = gdspy.Polygon(vertices)
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')