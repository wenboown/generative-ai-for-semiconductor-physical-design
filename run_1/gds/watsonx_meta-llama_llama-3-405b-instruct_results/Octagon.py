import gdspy
import math

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Octagon')

# Define the octagon's parameters
edge_length = 10  # mm
center = (0, 0)  # (x, y) coordinates
num_sides = 8

# Calculate the vertices of the octagon
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = center[0] + edge_length / (2 * math.tan(math.pi / num_sides)) * math.cos(angle)
    y = center[1] + edge_length / (2 * math.tan(math.pi / num_sides)) * math.sin(angle)
    vertices.append((x, y))

# Create the octagon as a polygon
poly = gdspy.Polygon(vertices, layer=0, datatype=0)

# Add the polygon to the cell
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('octagon.gds')