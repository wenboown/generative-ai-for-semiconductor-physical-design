import gdspy
import math

# Design specifications
edge_length = 10.0  # in mm
num_sides = 7  # for a heptagon
center = (0, 0)

# Calculating the vertices of the heptagon
def heptagon_vertices(center, edge_length, num_sides):
    angle = 2 * math.pi / num_sides
    R = edge_length / (2 * math.sin(math.pi / num_sides))  # circumradius
    return [
        (
            center[0] + R * math.cos(i * angle),
            center[1] + R * math.sin(i * angle)
        )
        for i in range(num_sides)
    ]

vertices = heptagon_vertices(center, edge_length, num_sides)

# Creating the GDSII layout
lib = gdspy.GdsLibrary()
cell = lib.new_cell('HEPTAGON')

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)
cell.add(heptagon)

# Save the design to a GDS file
gdspy.write_gds('heptagon.gds', [lib])

print("Heptagon with edge length 10 mm and center at (0,0) has been created and saved as heptagon.gds.")