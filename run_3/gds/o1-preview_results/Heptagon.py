import gdspy
import math

# Create a new GDSII library
lib = gdspy.GdsLibrary()

# Create a new cell
cell = lib.new_cell('HEPTAGON')

# Parameters
n_sides = 7
side_length_mm = 10.0  # Side length in millimeters
side_length = side_length_mm * 1000.0  # Convert to micrometers

# Calculate the radius of the circumscribed circle (in mm)
radius_mm = side_length_mm / (2 * math.sin(math.pi / n_sides))
radius = radius_mm * 1000.0  # Convert to micrometers

# Offset angle to align one vertex at the top
offset_angle = math.pi / 2

# Generate vertices of the heptagon
vertices = []
for i in range(n_sides):
    angle = offset_angle + i * 2 * math.pi / n_sides
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    vertices.append((x, y))

# Create the heptagon polygon
heptagon = gdspy.Polygon(vertices)

# Add the polygon to the cell
cell.add(heptagon)

# Save the GDS file
lib.write_gds('heptagon.gds')