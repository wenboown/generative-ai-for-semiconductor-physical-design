import numpy as np
import gdspy

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hexagon')

# Define the edge length of the hexagon
edge_length = 10

# Calculate the inner radius of the hexagon
inner_radius = edge_length / np.sqrt(3)

# Calculate the outer radius of the hexagon
outer_radius = 2 * edge_length / np.sqrt(3)

# Calculate the coordinates of the hexagon's vertices
vertices = []
for i in range(6):
    angle = i * np.pi / 3
    x = outer_radius * np.cos(angle)
    y = outer_radius * np.sin(angle)
    vertices.append((x, y))

# Create a polygon with the calculated vertices
hexagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')