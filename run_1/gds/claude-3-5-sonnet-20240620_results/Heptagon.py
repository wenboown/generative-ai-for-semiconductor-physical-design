import gdspy
import math

# Calculate the radius of the circumscribed circle
edge_length = 10  # 10 mm
n_sides = 7  # heptagon
R = edge_length / (2 * math.sin(math.pi / n_sides))

# Calculate the coordinates of the heptagon vertices
vertices = []
for i in range(n_sides):
    angle = 2 * math.pi * i / n_sides
    x = R * math.cos(angle)
    y = R * math.sin(angle)
    vertices.append((x, y))

# Create a gdspy library and cell
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Create a polygon using the calculated vertices
polygon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(polygon)

# Write the design to a GDS file
lib.write_gds('heptagon.gds')

print("Heptagon GDS file has been generated.")