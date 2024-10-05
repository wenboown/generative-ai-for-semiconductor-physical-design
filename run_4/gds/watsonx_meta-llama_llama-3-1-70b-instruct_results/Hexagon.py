import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('hexagon')

# Define the edge length and center of the hexagon
edge_length = 10
center_x, center_y = 0, 0

# Calculate the coordinates of the hexagon vertices
vertices = []
for i in range(6):
    angle = 2 * math.pi / 6 * i
    x = center_x + edge_length * math.cos(angle)
    y = center_y + edge_length * math.sin(angle)
    vertices.append((x, y))

# Create the hexagon polygon
hexagon = gdspy.Polygon(vertices, layer=1)

# Add the hexagon to the cell
cell.add(hexagon)

# Save the design to a GDS file
lib.write_gds('hexagon.gds')