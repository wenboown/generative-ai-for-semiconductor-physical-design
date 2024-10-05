import gdspy
import math

# Define the heptagon specifics
num_sides = 7
edge_length = 10
center = (0, 0)

# Calculate the radius of the circumscribed circle
radius = edge_length / (2 * math.sin(math.pi / num_sides))

# Calculate the vertices of the heptagon
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    vertices.append((x, y))

# Create a GDSII library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Create the heptagon polygon and add to the cell
heptagon = gdspy.Polygon(vertices)
cell.add(heptagon)

# Save the layout to a GDS file
lib.write_gds('heptagon.gds')

print("Heptagon GDS file has been generated successfully.")