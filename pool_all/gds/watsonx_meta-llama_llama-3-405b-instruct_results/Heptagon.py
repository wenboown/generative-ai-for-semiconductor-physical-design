import gdspy
import math

# Define the library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Heptagon parameters
num_sides = 7
edge_length = 10  # in mm
center = (0, 0)

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * math.sin(math.pi / num_sides))

# Calculate the vertices of the heptagon
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the heptagon to the cell
cell.add(heptagon)

# Save the design to a GDS file
lib.write_gds('heptagon.gds')

print("Heptagon GDS file has been generated successfully.")