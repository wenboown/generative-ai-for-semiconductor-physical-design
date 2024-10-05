import gdspy
import math

# Define the library and cell for the GDS layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('pentagon')

# Calculate the vertices of the regular pentagon
num_sides = 5
edge_length = 10
center_x, center_y = 0, 0
radius = edge_length / (2 * math.sin(math.pi / num_sides))
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = center_x + radius * math.cos(angle)
    y = center_y + radius * math.sin(angle)
    vertices.append((x, y))

# Create the polygon with precise coordinates
polygon = gdspy.Polygon(vertices, layer=1)

# Add the polygon to the cell
cell.add(polygon)

# Save the design to a GDS file
lib.write_gds('pentagon.gds')