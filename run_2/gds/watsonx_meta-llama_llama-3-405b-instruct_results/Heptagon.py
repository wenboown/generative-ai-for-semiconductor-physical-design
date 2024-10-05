import numpy as np
import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('heptagon')

# Define the heptagon parameters
num_sides = 7
edge_length = 10
center = (0, 0)

# Calculate the vertices of the heptagon
vertices = []
for i in range(num_sides):
    angle = 2 * np.pi * i / num_sides
    x = center[0] + edge_length * np.cos(angle)
    y = center[1] + edge_length * np.sin(angle)
    vertices.append((x, y))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')