import gdspy
import math

# Create a GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('OCTAGON')

# Design parameters
side_length = 10.0  # in mm
center = (0, 0)     # center at (0, 0)
num_sides = 8       # Octagon

# Convert units from mm to microns (GDSII units are in microns)
unit_conversion = 1000  # 1 mm = 1000 microns
side_length *= unit_conversion
center = (center[0] * unit_conversion, center[1] * unit_conversion)

# Calculate the radius of the octagon's circumcircle
# side_length = 2 * R * sin(pi / n)
radius = side_length / (2 * math.sin(math.pi / num_sides))

# Generate the vertices of the octagon
vertices = []
for i in range(num_sides):
    angle = 2 * math.pi * i / num_sides
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    vertices.append((x, y))

# Create the octagon polygon
octagon = gdspy.Polygon(vertices, layer=0)

# Add the octagon to the cell
cell.add(octagon)

# Save the layout to a GDSII file
lib.write_gds('octagon.gds')