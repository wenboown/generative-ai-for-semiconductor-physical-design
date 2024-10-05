import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('octagon')

# Define the coordinates for the octagon
center = (0, 0)
edge_length = 10
vertices = []
for i in range(8):
    angle = 2 * 3.14159 * i / 8
    x = center[0] + edge_length / 2 * (1 + 1/1.4142135623730951) * (math.cos(angle))
    y = center[1] + edge_length / 2 * (1 + 1/1.4142135623730951) * (math.sin(angle))
    vertices.append((x, y))

# Create the polygon for the octagon
poly = gdspy.Polygon(vertices, layer=0, datatype=0)
cell.add(poly)

# Save the design to a GDS file
lib.write_gds('octagon.gds')

import math