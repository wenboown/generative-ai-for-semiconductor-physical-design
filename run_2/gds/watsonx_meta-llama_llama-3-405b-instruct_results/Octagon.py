import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('Octagon')

# Define the octagon's parameters
edge_length = 10  # mm
center = (0, 0)

# Calculate the vertices of the octagon
vertices = []
for i in range(8):
    angle = 2 * math.pi / 8 * i
    x = center[0] + edge_length / 2 * (math.cos(angle) + math.cos(angle + math.pi / 4))
    y = center[1] + edge_length / 2 * (math.sin(angle) + math.sin(angle + math.pi / 4))
    vertices.append((x, y))

# Create the octagon as a polygon
octagon = gdspy.Polygon(vertices, 1, layer=0, datatype=0)

# Add the octagon to the cell
cell.add(octagon)

# Save the design to a GDS file
lib.write_gds('octagon.gds')