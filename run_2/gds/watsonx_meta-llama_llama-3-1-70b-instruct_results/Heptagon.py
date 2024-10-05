import gdspy
import math

# Define the GDS library and cell
lib = gdspy.Library()
cell = lib.cell("Heptagon_Cell")

# Define the Heptagon parameters
center = (0, 0)
edge_length = 10
num_sides = 7

# Calculate the angle between each vertex
angle = 2 * math.pi / num_sides

# Define the vertices of the Heptagon
vertices = []
for i in range(num_sides):
    x = center[0] + edge_length * math.cos(i * angle)
    y = center[1] + edge_length * math.sin(i * angle)
    vertices.append((x, y))

# Create the Heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the Heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds("heptagon.gds")