import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OCTAGON')

# Define the center and edge length
center_x, center_y = 0, 0
edge_length = 10.0  # mm
radius = edge_length / (2 * math.sin(math.pi / 8))

# Calculate the vertices of the octagon
vertices = []
for i in range(8):
    angle = 2 * math.pi * i / 8
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertices.append((x, y))

# Create the octagon as a polygon
octagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(octagon)

# Save to a GDS file
lib.write_gds('octagon.gds')

# Optionally, to view the layout using built-in viewer